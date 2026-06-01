import imaplib
import email
import getpass
import sys

YAHOO_IMAP = "imap.mail.yahoo.com"
YAHOO_PORT = 993


def connect(user: str, app_password: str) -> imaplib.IMAP4_SSL:
    mail = imaplib.IMAP4_SSL(YAHOO_IMAP, YAHOO_PORT)
    mail.login(user, app_password)
    return mail


def delete_by_sender(mail: imaplib.IMAP4_SSL, sender: str, folder: str = "INBOX") -> int:
    mail.select(folder)
    _, data = mail.search(None, f'FROM "{sender}"')
    ids = data[0].split()

    if not ids:
        print(f"Aucun mail trouvé de : {sender}")
        return 0

    print(f"{len(ids)} mail(s) trouvé(s) de {sender}. Suppression...")
    for num in ids:
        mail.store(num, "+FLAGS", "\\Deleted")

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
    user = input("Adresse Yahoo : ").strip()
    app_password = getpass.getpass("Mot de passe d'application Yahoo : ")

    try:
        mail = connect(user, app_password)
        print("Connecté !\n")
    except imaplib.IMAP4.error as e:
        print(f"Erreur de connexion : {e}")
        sys.exit(1)

    while True:
        print("\nOptions :")
        print("  1. Supprimer les mails d'un expéditeur")
        print("  2. Lister les dossiers")
        print("  3. Quitter")
        choice = input("\nChoix : ").strip()

        if choice == "1":
            sender = input("Adresse de l'expéditeur à supprimer : ").strip()
            folder = input("Dossier (INBOX par défaut, Entrée pour confirmer) : ").strip() or "INBOX"
            delete_by_sender(mail, sender, folder)
        elif choice == "2":
            list_folders(mail)
        elif choice == "3":
            mail.logout()
            print("Déconnecté.")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
