import numpy as np

A = [chr(i) for i in range(ord('A'),ord('Z') + 1)]

def alpha_to_perm(alphabet):
    return [A.index(alphabet[i]) for i in range(len(alphabet))]

def perm_alea():
    return np.random.permutation(26)

def chiffrement_permutation(message, permutation):
    message_chiffre = ""
    alphabet_permute = [A[permutation[i]] for i in range(len(A))]
    print("Nouvel alphabet : ")
    print(alphabet_permute)
    print("\n")
    for lettre in message:
        if lettre.isalpha():
            # Décalage de la lettre en fonction de la clé
            # ascii_decalage = (ord(lettre.upper()) - ord('A') + decalage) % 26
            # Conversion du code ASCII décalé en caractère
            lettre_chiffree = alphabet_permute[A.index(lettre.upper())]
            # Gestion de la casse
            if lettre.isupper():
                message_chiffre += lettre_chiffree
            else:
                message_chiffre += lettre_chiffree.lower()
        else:
            # Ajout des caractères non alphabétiques sans modification
            message_chiffre += lettre
    return message_chiffre,alphabet_permute


def launch():
    # Demande à l'utilisateur de saisir le message et la clé de chiffrement
    message_original = input("Entrez le message à chiffrer : ")
    # cle_chiffrement = int(input("Entrez la clé de chiffrement : "#))

    M = perm_alea().tolist()
    print("Permutation générée : ")
    print(M)
    print("\n")
    # Applique le chiffrement de César au message
    message_chiffre,alphabet_permute = chiffrement_permutation(message_original, M)

    # Affiche le message chiffré
    print("Message chiffré :", message_chiffre)

