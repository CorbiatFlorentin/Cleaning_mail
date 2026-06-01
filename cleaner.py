import imaplib
import sys
import os
from dotenv import load_dotenv

load_dotenv()

YAHOO_IMAP = "imap.mail.yahoo.com"
YAHOO_PORT = 993


def connect() -> imaplib.IMAP4_SSL:
    user = os.getenv("YAHOO_EMAIL")
    password = os.getenv("YAHOO_APP_PASSWORD")

    if not user or not password:
        print("Erreur : YAHOO_EMAIL ou YAHOO_APP_PASSWORD manquant dans le fichier .env")
        sys.exit(1)

    mail = imaplib.IMAP4_SSL(YAHOO_IMAP, YAHOO_PORT)
    mail.login(user, password)
    return mail


def delete_by_sender(mail: imaplib.IMAP4_SSL, sender: str, folder: str = "INBOX") -> int:
    mail.select(folder)
    _, data = mail.search(None, f'FROM "{sender}"')
    ids = data[0].split()

    if not ids:
        print(f"Aucun mail trouvé de : {sender}")
        return 0

    print(f"{len(ids)} mail(s) trouvé(s) de {sender}. Suppression...")
    id_list = b",".join(ids)
    mail.store(id_list, "+FLAGS", "\\Deleted")
    mail.expunge()
    print(f"✓ {len(ids)} mail(s) supprimé(s).")
    return len(ids)


def list_folders(mail: imaplib.IMAP4_SSL):
    _, folders = mail.list()
    print("\nDossiers disponibles :")
    for f in folders:
        print(" -", f.decode())


def main():
    print("=== Yahoo Mail Cleaner ===\n")

    try:
        mail = connect()
        print("Connecté !\n")
    except imaplib.IMAP4.error as e:
        print(f"Erreur de connexion : {e}")
        sys.exit(1)

    while True:
        print("\n[1] Supprimer par expéditeur  [2] Lister les dossiers  [3] Quitter")
        print("Ou colle directement une adresse email pour la supprimer :")
        choice = input("> ").strip()

        if "@" in choice:
            delete_by_sender(mail, choice)
        elif choice == "1":
            sender = input("Adresse de l'expéditeur : ").strip()
            folder = input("Dossier (Entrée = INBOX) : ").strip() or "INBOX"
            delete_by_sender(mail, sender, folder)
        elif choice == "2":
            list_folders(mail)
        elif choice == "3":
            mail.logout()
            print("Déconnecté.")
            break
        else:
            print("Choix invalide. Entre 1, 2, 3 ou colle une adresse email.")


if __name__ == "__main__":
    main()
