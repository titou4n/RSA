import os
import rsa

def decrypt_directory(directory_path, private_key, extension):
    print("")
    # Parcours de tous les fichiers du répertoire
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Vérification de l'extension du fichier chiffré
            dot_extension = "."+str(extension)
            if file.endswith(dot_extension):
                # Lecture du fichier chiffré
                with open(file_path, 'rb') as file:
                    encrypted_data = file.read()

                # Déchiffrement des données avec la clé privée
                decrypted_data = rsa.decrypt(encrypted_data, private_key)

                # Écriture des données déchiffrées dans un nouveau fichier
                len_dot_extension = len(dot_extension)
                decrypted_file_path = file_path[:-len_dot_extension]  # Suppression de l'extension '.encrypt'
                with open(decrypted_file_path, 'wb') as file:
                    file.write(decrypted_data)
                print(f"Le fichier {file_path} a été déchiffré avec succès.")
                os.remove(file_path)
                print("\nDirectory encryption completed.") 
    
