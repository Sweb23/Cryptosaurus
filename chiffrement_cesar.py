def chiffrement(message, decalage):
    message_chiffre = ""
    for lettre in message:
        if lettre.isalpha():
            # Décalage de la lettre en fonction de la clé
            ascii_decalage = (ord(lettre.upper()) - ord('A') + decalage) % 26
            # Conversion du code ASCII décalé en caractère
            lettre_chiffree = chr(ascii_decalage + ord('A'))
            # Gestion de la casse
            if lettre.isupper():
                message_chiffre += lettre_chiffree
            else:
                message_chiffre += lettre_chiffree.lower()
        else:
            # Ajout des caractères non alphabétiques sans modification
            message_chiffre += lettre
    return message_chiffre

def launch():
    # Demande à l'utilisateur de saisir le message et la clé de chiffrement
    message_original = input("Entrez le message à chiffrer : ")
    cle_chiffrement = int(input("Entrez la clé de chiffrement : "))

    # Applique le chiffrement de César au message
    message_chiffre = chiffrement(message_original, cle_chiffrement)

    # Affiche le message chiffré
    print("Message chiffré :", message_chiffre)
