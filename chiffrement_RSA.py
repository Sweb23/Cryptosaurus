# coding: utf-8

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


def generer_cles_RSA():
    # Génère une paire de clés RSA
    cle_privee = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    cle_publique = cle_privee.public_key()

    return cle_publique, cle_privee


def chiffrer_RSA(message, cle_publique):
    # Chiffre le message avec la clé publique
    message_bytes = message.encode('utf-8')
    message_chiffre = cle_publique.encrypt(
        message_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return message_chiffre


def dechiffrer_RSA(message_chiffre, cle_privee):
    # Déchiffre le message avec la clé privée
    message_dechiffre = cle_privee.decrypt(
        message_chiffre,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return message_dechiffre.decode('utf-8')

def launch():
    # Génère une paire de clés RSA
    cle_publique, cle_privee = generer_cles_RSA()

    # Demande à l'utilisateur de saisir un message
    message_original = input("Entrez un message à chiffrer : ")

    # Chiffre le message avec la clé publique
    message_chiffre = chiffrer_RSA(message_original, cle_publique)

    print("Message chiffré :", message_chiffre)

    # Déchiffre le message avec la clé privée
    message_dechiffre = dechiffrer_RSA(message_chiffre, cle_privee)

    print("Message déchiffré :", message_dechiffre)
