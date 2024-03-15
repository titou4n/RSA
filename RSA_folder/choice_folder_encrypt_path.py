import os

def append_folder_encrypt_path(folder_encrypt_path):
    if os.path.exists("settings\\choice_folder_encrypt_path.txt"):
        os.remove("settings\\choice_folder_encrypt_path.txt")
    fichier_name = open("settings\\choice_folder_encrypt_path.txt", "w+")
    fichier_name.write(str(folder_encrypt_path))
    fichier_name.close()

def find_folder_encrypt_path():
    if os.path.exists("settings\\choice_folder_encrypt_path.txt")==True:
        with open("settings\\choice_folder_encrypt_path.txt",'r+') as file:
            list_folder_encrypt_path = file.readlines()
            folder_encrypt_path = list_folder_encrypt_path[0]
        return folder_encrypt_path
    else :
        return None
