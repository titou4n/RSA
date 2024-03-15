import rsa
import os
def encrypt_file(filename, public_key):
    # Lecture du fichier
    with open(filename, 'rb') as file:
        data = file.read()
    # Chiffrement des données avec la clé publique
    encrypted_data = rsa.encrypt(data, public_key)
    # Écriture des données chiffrées dans un nouveau fichier
    encrypted_filename = filename + '.tit'
    with open(encrypted_filename, 'wb') as file:
        file.write(encrypted_data)
    os.remove(filename)
    print("Le fichier a été chiffré avec succès.")


# Génération d'une paire de clés RSA
(public_key, private_key) = rsa.newkeys(4096)
print("public_key   : "+str(public_key.save_pkcs1()))
print("private_key  : "+str(private_key.save_pkcs1()))

# Sauvegarde des clés dans des fichiers (optionnel)
with open('public_key.pem', 'wb') as file:
    file.write(public_key.save_pkcs1())
with open('private_key.pem', 'wb') as file:
    file.write(private_key.save_pkcs1())

#public_key = public_key.save_pkcs1()
#private_key = private_key.save_pkcs1()
print(type(public_key))
print(type(private_key))
# Chemin vers le fichier à chiffrer
filename = "txt.txt"
print(os.path.exists(filename))
# Chiffrement du fichier
encrypt_file(filename, public_key)
