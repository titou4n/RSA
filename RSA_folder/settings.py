import os
import shutil

def reset_default_settings():
    print("\nIf you reset settings, all information will be remove")
    reset = str(input("Are you sure you want to reset (Y/N) : "))
    if  reset =="Y" or reset == "y":
        if os.path.exists("public_key.pem") == True:
            os.remove("public_key.pem")
        if os.path.exists("settings") == True:
            shutil.rmtree("settings")
        if os.path.exists("Folder_encrypt") == True:
            shutil.rmtree("Folder_encrypt")
            
def create_folder_encrypt():
    os.makedirs("Folder_encrypt", exist_ok=True)
    file = open("Folder_encrypt\\WARNING.txt", "w+") 
    file.write("WARNING : If you lose, delete or modify the file containing the Private_key;")
    file.write("It will no longer be possible to decrypt the folder.")  
    file.close()

def create_file_extension():
    os.makedirs("settings", exist_ok=True)
    file = open("settings\\choice_extension.txt", "w+") 
    file.write("encrypt") 
    file.close()

def create_file_of_folder_encrypt_path():
    os.makedirs("settings", exist_ok=True)
    file = open("settings\\choice_folder_encrypt_path.txt", "w+") 
    file.write("Folder_encrypt") 
    file.close()
    