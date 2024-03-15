import os

def append_private_key_path(private_key_path):
    if os.path.exists("settings\\choice_private_key_path.txt"):
        os.remove("settings\\choice_private_key_path.txt")
    fichier_name = open("settings\\choice_private_key_path.txt", "w+")
    fichier_name.write(str(private_key_path))
    fichier_name.close()

def find_private_key_path():
    with open("settings\\choice_private_key_path.txt",'r+') as file:
        list_private_key_path = file.readlines()
        private_key_path = list_private_key_path[0]
    return private_key_path
