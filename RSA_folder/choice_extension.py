import os


def append_extension(extension):
    if os.path.exists("settings\\choice_extension.txt"):
        os.remove("settings\\choice_extension.txt")
    fichier_name = open("settings\\choice_extension.txt", "w+")
    fichier_name.write(str(extension))
    fichier_name.close()

def find_extension():
    if os.path.exists("settings\\choice_folder_encrypt_path.txt")==True:
        with open("settings\\choice_extension.txt",'r+') as file:
            list_extension = file.readlines()
            extension = list_extension[0]
        return extension
    else:
        return None