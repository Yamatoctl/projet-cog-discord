Étape 2 — Créer ton bot sur Discord

1. Va sur **discord.com/developers/applications**
2. Clique **"New Application"** → donne un nom
3. Va dans **"Bot"** → clique **"Add Bot"**
4. Copie le **TOKEN** (garde le secret !)
5. Dans **"Privileged Gateway Intents"** active :
   - ✅ Server Members Intent
   - ✅ Message Content Intent

### Étape 3 — Structure de ton projet
```
mon-bot/
├── main.py
└── cogs/
    └── greetings.py