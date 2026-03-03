# Pour ce TP utiliser la bibliothèque pycryptodome
# https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#classic-cipher-modes

#https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html

#Dans ce TP, nous allons utiliser la bibliothèque pycryptodome pour chiffrer et déchiffrer 
# un message en utilisant l'algorithme AES en mode CBC. Le code ci-dessous montre comment 
# générer une clé aléatoire, chiffrer un message, puis le déchiffrer en utilisant la même
#  clé et le vecteur d'initialisation (IV) utilisé pour le chiffrement. Le résultat du
#  chiffrement est encodé en base64 pour faciliter le stockage et la transmission.

# L'objectif est de faire un chat chiffre bout-en-bout avec votre camarade en utilisant ce code comme base.
#  en utlisisant un serveur d'echange avec FLASK. 
# Client---> Serveur <---Client
#1. Chaque client envoie son login au serveur, le serveur stocke les logins. 
#2. Chaque client fournit un mot de passe pour generer une cle AES sans envoyer la cle au serveur. Son correspondant doit faire de meme pour generer la meme cle AES.
#3. Chaque client peut demander la liste des logins (des autres clients connectés) au serveur.
#4. chaque client peut envoyer un message chiffré à un autre client en utilisant la clé AES partagee (on verra la negociation au chapitre suivant).
#5. le serveur stocke les messages chiffrés et les envoient au client destinataire a leur demande.
#6. a chaque instant le client demande au serveur s'il de nouveaux message pour lui. si oui le serveur lui envoieles messages chiffres.



import json
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


if __name__ == "__main__":
    data = b"secret"
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv':iv, 'ciphertext':ct})
    print("Le chiffe est : ",result)
    try:
        b64 = json.loads(result)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        print("The message etait: ", pt)
    except (ValueError, KeyError):
        print("Incorrect decryption")