<div align="center">

# 🧹 Yahoo Mail Cleaner

<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Yahoo%20Mail-IMAP-6001D2?style=for-the-badge&logo=yahoo&logoColor=white"/>
<img src="https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Active-22c55e?style=for-the-badge"/>

<br/>

> **Nettoyez votre boîte Yahoo en quelques secondes.**  
> Supprimez des centaines de mails indésirables par expéditeur, sans effort.

<br/>

```
╔═══════════════════════════════════════╗
║       === Yahoo Mail Cleaner ===      ║
║                                       ║
║  Connecté !                           ║
║                                       ║
║  > newsletter@spam.com                ║
║  ✓ 142 mail(s) supprimé(s).           ║
║                                       ║
║  > promo@cdiscount.com                ║
║  ✓ 89 mail(s) supprimé(s).            ║
╚═══════════════════════════════════════╝
```

</div>

---

## ✨ Fonctionnalités

| Fonctionnalité | Description |
|---|---|
| 🎯 **Suppression par expéditeur** | Supprime tous les mails d'une adresse en une commande |
| ⚡ **Suppression en lot** | Traite des centaines de mails en une seule fois |
| 📁 **Multi-dossiers** | Fonctionne sur INBOX et tous vos dossiers Yahoo |
| 🔒 **Sécurisé** | Credentials isolés dans un `.env`, jamais exposés |
| 🖥️ **Interface simple** | Colle l'adresse, Entrée — c'est fait |

---

## 🚀 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/CorbiatFlorentin/Cleaning_mail.git
cd Cleaning_mail
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Configurer les credentials

Copie le fichier d'exemple et remplis-le :

```bash
cp .env.example .env
```

```env
YAHOO_EMAIL=ton_adresse@yahoo.fr
YAHOO_APP_PASSWORD=xxxx xxxx xxxx xxxx
```

> ⚠️ **Important** — Yahoo exige un **mot de passe d'application**, pas ton mot de passe habituel.

---

## 🔑 Créer un mot de passe d'application Yahoo

<div align="center">

```
1. Va sur › security.yahoo.com
       ↓
2. "Mot de passe d'application"
       ↓
3. Génère-en un pour "Autre application"
       ↓
4. Copie-le dans ton .env
```

</div>

---

## 🖥️ Utilisation

```bash
python cleaner.py
```

Une fois connecté, **colle directement l'adresse** de l'expéditeur à supprimer :

```
[1] Supprimer par expéditeur  [2] Lister les dossiers  [3] Quitter
Ou colle directement une adresse email pour la supprimer :
> newsletter@tripadvisor.com
✓ 56 mail(s) supprimé(s).

> promo@cdiscount.com
✓ 102 mail(s) supprimé(s).

> 3
Déconnecté.
```

---

## 📁 Structure du projet

```
Cleaning_mail/
├── 📄 cleaner.py          # Script principal
├── 📄 requirements.txt    # Dépendances Python
├── 🔒 .env                # Credentials (non versionné)
├── 📄 .env.example        # Modèle de configuration
└── 🚫 .gitignore          # Protège le .env
```

---

## 🛡️ Sécurité

- Le fichier `.env` est dans le `.gitignore` — **il ne sera jamais pushé sur GitHub**
- Le mot de passe d'application Yahoo peut être **révoqué à tout moment** depuis les paramètres de sécurité Yahoo
- Aucune donnée n'est stockée ou transmise à un tiers

---

## 🧰 Stack technique

<div align="center">

<img src="https://img.shields.io/badge/imaplib-builtin-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/python--dotenv-1.2.1-ECD53F?style=flat-square&logo=dotenv&logoColor=black"/>

</div>

---

<div align="center">

Fait avec ❤️ par [Florentin Corbiat](https://github.com/CorbiatFlorentin)

</div>
