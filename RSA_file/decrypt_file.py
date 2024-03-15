import rsa

def decrypt_file(filename, private_key):
    # Lecture du fichier chiffré
    with open(filename, 'rb') as file:
        encrypted_data = file.read()

    # Déchiffrement des données avec la clé privée
    decrypted_data = rsa.decrypt(encrypted_data, private_key)

    # Écriture des données déchiffrées dans un nouveau fichier
    decrypted_filename = filename[:-4]  # Suppression de l'extension '.enc'
    with open(decrypted_filename, 'wb') as file:
        file.write(decrypted_data)
    print("Le fichier a été déchiffré avec succès.")

# Chargement de la clé privée depuis le fichier
with open('private_key.pem', 'rb') as file:
    private_key = rsa.PrivateKey.load_pkcs1(file.read())

# Chemin vers le fichier chiffré
filename = "txt.txt.tit"

# Décryptage du fichier
decrypt_file(filename, private_key)
