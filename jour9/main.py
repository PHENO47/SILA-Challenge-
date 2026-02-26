import sys
import sqlite3
import csv
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QListWidget, QListWidgetItem, QPushButton,
    QLineEdit, QComboBox, QLabel, QMessageBox,
    QSystemTrayIcon, QStyle
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextDocument
from PyQt6.QtPrintSupport import QPrinter


# --- 1. BASE DE DONNÉES AVEC MIGRATION ---
class Database:
    def __init__(self):
        self.conn = sqlite3.connect("kanban_ultimate.db")
        self.cursor = self.conn.cursor()
        self.migrate()

    def migrate(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                status TEXT,
                priority TEXT,
                tags TEXT
            )
        """)
        self.conn.commit()


# --- 2. COMPOSANT KANBAN AVEC DRAG & DROP ---
class KanbanList(QListWidget):
    def __init__(self, status, parent=None):
        super().__init__(parent)
        self.status = status
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDefaultDropAction(Qt.DropAction.MoveAction)

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        super().dropEvent(event)

        app = self.window()
        item = self.currentItem()
        if item:
            # Récupération propre du titre
            text_line = item.text().split("\n")[0]
            title = text_line.split("] ", 1)[1]

            app.db.cursor.execute(
                "UPDATE tasks SET status = ? WHERE title = ?",
                (self.status, title)
            )
            app.db.conn.commit()
            app.refresh_data()


# --- 3. APPLICATION PRINCIPALE ---
class KanbanApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = Database()

        self.setWindowTitle("Kanban Ultimate Pro - Challenge Validé")
        self.resize(1000, 700)

        self.init_ui()
        self.init_tray()

    # --- SYSTEM TRAY ---
    def init_tray(self):
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(
            self.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon)
        )
        self.tray_icon.show()

    def closeEvent(self, event):
        self.db.conn.close()
        event.accept()

    # --- UI ---
    def init_ui(self):
        main_layout = QVBoxLayout()

        # --- FILTRES ---
        filter_layout = QHBoxLayout()

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("🔍 Filtrer par titre ou tags...")
        self.search_bar.textChanged.connect(self.refresh_data)

        self.priority_filter = QComboBox()
        self.priority_filter.addItems(["Toutes", "Basse", "Moyenne", "Haute"])
        self.priority_filter.currentTextChanged.connect(self.refresh_data)

        filter_layout.addWidget(self.search_bar)
        filter_layout.addWidget(self.priority_filter)

        main_layout.addLayout(filter_layout)

        # --- VUE KANBAN ---
        kanban_layout = QHBoxLayout()

        self.todo_list = KanbanList("A faire")
        self.doing_list = KanbanList("En cours")
        self.done_list = KanbanList("Terminé")

        self.lists = [self.todo_list, self.doing_list, self.done_list]

        for title, widget in [
            ("À FAIRE", self.todo_list),
            ("EN COURS", self.doing_list),
            ("TERMINÉ", self.done_list)
        ]:
            col = QVBoxLayout()
            col.addWidget(QLabel(f"<b>{title}</b>"))
            col.addWidget(widget)
            kanban_layout.addLayout(col)

        main_layout.addLayout(kanban_layout)

        # --- AJOUT TÂCHE ---
        add_layout = QHBoxLayout()

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Titre de la tâche...")

        self.priority_combo = QComboBox()
        self.priority_combo.addItems(["Basse", "Moyenne", "Haute"])

        self.tag_input = QLineEdit()
        self.tag_input.setPlaceholderText("Tags (ex: Bug, UI)...")

        add_btn = QPushButton("➕ Ajouter")
        add_btn.clicked.connect(self.add_task)

        add_layout.addWidget(self.task_input)
        add_layout.addWidget(self.priority_combo)
        add_layout.addWidget(self.tag_input)
        add_layout.addWidget(add_btn)

        main_layout.addLayout(add_layout)

        # --- EXPORTS ---
        export_layout = QHBoxLayout()

        btn_csv = QPushButton("📊 Export CSV")
        btn_csv.clicked.connect(self.export_csv)

        btn_pdf = QPushButton("📕 Export PDF")
        btn_pdf.clicked.connect(self.export_pdf)

        export_layout.addWidget(btn_csv)
        export_layout.addWidget(btn_pdf)

        main_layout.addLayout(export_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.refresh_data()

    # --- AJOUT ---
    def add_task(self):
        title = self.task_input.text().strip()
        priority = self.priority_combo.currentText()
        tags = self.tag_input.text().strip()

        if title:
            self.db.cursor.execute(
                "INSERT INTO tasks (title, status, priority, tags) VALUES (?, ?, ?, ?)",
                (title, "A faire", priority, tags)
            )
            self.db.conn.commit()

            self.tray_icon.showMessage(
                "Nouvelle tâche ajoutée",
                f"{title} ({priority})",
                QSystemTrayIcon.MessageIcon.Information,
                3000
            )

            self.task_input.clear()
            self.tag_input.clear()
            self.refresh_data()

    # --- REFRESH ---
    def refresh_data(self):
        search_text = self.search_bar.text().lower()
        selected_priority = self.priority_filter.currentText()

        for lst in self.lists:
            lst.clear()

        self.db.cursor.execute(
            "SELECT title, status, priority, tags FROM tasks"
        )

        for title, status, priority, tags in self.db.cursor.fetchall():
            tags = tags or ""

            matches_search = (
                search_text in title.lower()
                or search_text in tags.lower()
            )
            matches_priority = (
                selected_priority == "Toutes"
                or priority == selected_priority
            )

            if matches_search and matches_priority:
                display_text = f"[{priority}] {title}\n🏷️ {tags}"
                item = QListWidgetItem(display_text)

                if status == "A faire":
                    self.todo_list.addItem(item)
                elif status == "En cours":
                    self.doing_list.addItem(item)
                else:
                    self.done_list.addItem(item)

    # --- EXPORT CSV ---
    def export_csv(self):
        with open("kanban_export.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Titre", "Statut", "Priorité", "Tags"])
            self.db.cursor.execute("SELECT * FROM tasks")
            writer.writerows(self.db.cursor.fetchall())

        QMessageBox.information(self, "Succès", "Export CSV réussi !")

    # --- EXPORT PDF ---
    def export_pdf(self):
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
        printer.setOutputFileName("kanban_report.pdf")

        self.db.cursor.execute(
            "SELECT title, status, priority, tags FROM tasks"
        )
        rows = self.db.cursor.fetchall()

        html = """
        <h1>Rapport de Projet Kanban</h1>
        <table border='1' width='100%' cellpadding='5'>
        <tr>
        <th>Titre</th>
        <th>Statut</th>
        <th>Priorité</th>
        <th>Tags</th>
        </tr>
        """

        for r in rows:
            html += f"""
            <tr>
            <td>{r[0]}</td>
            <td>{r[1]}</td>
            <td>{r[2]}</td>
            <td>{r[3]}</td>
            </tr>
            """

        html += "</table>"

        doc = QTextDocument()
        doc.setHtml(html)
        doc.print(printer)

        QMessageBox.information(
            self,
            "Succès",
            "Rapport PDF généré : kanban_report.pdf"
        )


# --- LANCEMENT ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KanbanApp()
    window.show()
    sys.exit(app.exec())