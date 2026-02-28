📂 Maintenant : Ajouter un dossier dans ton projet

Dans ton repo GitHub, crée :

docs/
│
└── api_keys_setup.md
📄 Contenu suggéré pour api_keys_setup.md

Voici ce que tu peux mettre dedans 👇
(Tu pourras copier-coller)

📘 How to Get API Keys
🌦 OpenWeatherMap API Key

Go to https://openweathermap.org

Sign up for a free account

Verify your email

Go to Profile → My API Keys

Copy your generated API key

⚠ Activation may take up to 15 minutes.

📰 NewsAPI Key

Go to https://newsapi.org

Click on "Get API Key"

Create a free account

Your API key will appear in your dashboard

Free plan allows 100 requests/day.

🐙 (Optional) GitHub Token

Go to https://github.com/settings/tokens

Click "Generate new token"

Select minimal permissions

Copy your token securely

🔐 Important Security Notice

Never commit your API keys to GitHub.

Use:

Environment variables

.env files

User input (like this project does)

🎯 Pourquoi c’est une très bonne idée ?

✔ Tu montres que tu comprends la sécurité
✔ Tu aides les utilisateurs de ton projet
✔ Ton repo devient professionnel
✔ Tu respectes les bonnes pratiques open-source

💎 Petit bonus (optionnel mais pro)

Ajoute un fichier .gitignore :

.env
__pycache__/
🏆 Résultat final

Ton repo aura :

async-api-client/
│
├── main.py
├── client.py
├── utils.py
├── docs/
│   └── api_keys_setup.md
├── requirements.txt
└── README.md