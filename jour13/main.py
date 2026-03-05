from indexer import Indexer
from searcher import Searcher
from utils import highlight, snippet
import os


def menu():

    print("\n==============================")
    print(" REGEX SEARCH ENGINE")
    print("==============================")
    print("1. Indexer un dossier")
    print("2. Rechercher")
    print("3. Quitter")


def main():

    indexer = Indexer()

    while True:

        menu()

        choice = input("\nChoix : ")

        if choice == "1":

            path = input("Chemin du dossier : ")

            if not os.path.exists(path):

                print("❌ Dossier introuvable")

                continue

            print("\nIndexation en cours...")

            indexer.index_directory(path)

            indexer.save()

            print("✅ Index créé avec succès")

        elif choice == "2":

            if not os.path.exists("index.pkl"):

                print("⚠️ Aucun index trouvé")

                continue

            indexer.load()

            searcher = Searcher(indexer.index, indexer.documents)

            pattern = input("\nRegex de recherche : ")

            results = searcher.search(pattern)

            if not results:

                print("❌ Aucun résultat trouvé")

                continue

            print(f"\n🔎 {len(results)} résultat(s) trouvé(s)\n")

            for score, path, matches, text in results:

                print("📄", path)

                print("Score TF-IDF:", round(score, 3))

                for m in matches[:2]:

                    snip = snippet(text, m)

                    print("...", highlight(snip, pattern), "...")

                print()

        elif choice == "3":

            print("👋 Fin du programme")

            break

        else:

            print("Choix invalide")


if __name__ == "__main__":

    main()