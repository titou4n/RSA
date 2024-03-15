import rsa
from encrypt_folder import encrypt_directory
from decrypt_folder import decrypt_directory
import os
import shutil
from choice_extension import find_extension, append_extension
from choice_private_key_path import find_private_key_path, append_private_key_path
from choice_folder_encrypt_path import find_folder_encrypt_path, append_folder_encrypt_path
from settings import reset_default_settings, create_file_extension, create_file_of_folder_encrypt_path, create_folder_encrypt

def verif_settings():
    if os.path.exists("settings") == False:
        return False
    else:
        if os.path.exists("settings\\choice_extension.txt") == False:
            return False
        if os.path.exists("settings\choice_private_key_path.txt") == False:
            return False
        if os.path.exists("settings\choice_private_key_path.txt") == False:
            return False
        else:
            return True

def first_time():
    print("\nIt's your First time !!!!")
    create_folder_encrypt()
    create_file_of_folder_encrypt_path()
    print("\nWe will create an RSA key pair for you")
    print("- A public key in the same file as this one, named 'public_key', which will be used to encrypt the data.")
    print("- A private one in your USB key, named 'private_key', which will be used to decrypt the data.")
    generate_rsa_key_pair()
    create_file_extension()
    print("\nYou can now put files in the folder '"+find_folder_encrypt_path()+"' and encrypt and decrypt them whenever you like.")
    print("WARNING : If you lose, delete or modify the file containing the Private_key;")
    print("It will no longer be possible to decrypt the folder.")
    encrypt_decrypt_folder()


def generate_rsa_key_pair():
    # Génération d'une paire de clés RSA
    (public_key, private_key) = rsa.newkeys(2048)
    print("\n1    -First of all, plug in your USB drive, which will contain your private key.")
    letter_USB_drive = str(input("2    -Give us the letter of your USB drive so that we can register it (Ex: D; E; F; ...) : ")).upper()
    letter_USB_drive = str(letter_USB_drive)+":\\"
    if os.path.exists(letter_USB_drive) == True:
        private_key_path = str(letter_USB_drive)+"private_key.pem"
        append_private_key_path(private_key_path)
        # Sauvegarde de la clé publique dans un fichier (optionnel)
        with open('public_key.pem', 'wb') as file:
            file.write(public_key.save_pkcs1())
        with open(private_key_path, 'wb') as file:
            file.write(private_key.save_pkcs1())
        return public_key
    else:
        print("USB drive letter given is invalid")
        generate_rsa_key_pair()


def verif_usb_key(private_key_path):
    if os.path.exists(private_key_path) == True:
        with open(private_key_path, 'rb') as file:
            private_key = rsa.PrivateKey.load_pkcs1(file.read())
    else:
        print("Please insert your key containing the 'private_key'.")
        while os.path.exists(private_key_path) == False :
            pass
        with open(private_key_path, 'rb') as file:
            private_key = rsa.PrivateKey.load_pkcs1(file.read())
    return private_key

def encrypt_folder(directory_path):
    if verif_settings() == True:
        extension = find_extension()
        if os.path.exists(directory_path) == True:
            print("1    - I have my RSA 'public_key'")
            print("2    - I don't have RSA 'public_key'")
            choice_public_key = input("Choice : ")
            if choice_public_key == "1" :
                public_key_path = 'public_key.pem'
                print("Public key path uses : " + public_key_path)
                with open(public_key_path, 'rb') as file:
                    public_key = rsa.PublicKey.load_pkcs1(file.read())
                print(public_key)
                encrypt_directory(directory_path, public_key, extension)
                print("\nDirectory encryption completed.")
            if choice_public_key == "2" :
                public_key = generate_rsa_key_pair()
                print("\nYou can get your 'public_key' RSA.")
                print("You can get your 'private_key' RSA and place it on your USB key.")
                encrypt_directory(directory_path, public_key, extension)
            else:
                encrypt_decrypt_folder()
        else:
            print("Folder path is invalid or doesn't exist")
    else:
        print("\nError: The settings file has been modified or you haven't set up your app.")
        print("If this is your first time, please go to the 'first time' compartment.")
        print("Otherwise reset, and set the parameters to default.")


def decrypt_folder(directory_path):
    if verif_settings() == True:
        extension = find_extension()
        if os.path.exists(directory_path) == True:
            print("\nFolder path : Valid")
            # Chargement de la clé privée depuis le fichier
            private_key_path = find_private_key_path()
            private_key = verif_usb_key(private_key_path)
            print("'private_key' : Valid")
            decrypt_directory(directory_path, private_key, extension)
        else:
            print("Folder path is invalid or doesn't exist")
    else:
        print("\nError: The settings file has been modified or you haven't set up your app.")
        print("If this is your first time, please go to the 'first time' compartment.")
        print("Otherwise reset, and set the parameters to default.")
        

def choice_folder_encrypt_path():
    old_folder_encrypt_path = find_folder_encrypt_path()
    folder_encrypt_path = str(input("\nPlease enter Folder to encrypt path (Q->Quit): "))
    print(folder_encrypt_path)
    if os.path.exists(folder_encrypt_path) == True:
        append_folder_encrypt_path(folder_encrypt_path)
        print("Data updated : "+str(old_folder_encrypt_path)+" -> "+str(folder_encrypt_path))
        return "ok"
    if folder_encrypt_path == "Q" or folder_encrypt_path == "q":
        encrypt_decrypt_folder()
    else :
        print(os.path.exists(folder_encrypt_path))
        print("Folder path is invalid or doesn't exist")
        choice_folder_encrypt_path()

def choice_private_key_path():
    old_private_key_path = find_private_key_path()
    
    private_key_path = str(input("\nPlease enter new 'private_key_path' (without quotes) (Q->Quit) :  "))
    if os.path.exists(private_key_path) == True:
        if os.path.exists(old_private_key_path)==True:
            os.remove(old_private_key_path)
        else:
            append_private_key_path(private_key_path)
            print("Data updated : "+str(old_private_key_path)+" -> "+str(private_key_path))
    if private_key_path == "Q" or private_key_path == "q":
        encrypt_decrypt_folder()
    else :
        print("'private_key_path' is invalid or doesn't exist")
        choice_private_key_path()
    

def choice_extension():
    old_extension = find_extension()
    extension = str(input("\nPlease enter extension (Q->Quit):   ."))
    if extension.lower() == True:
        append_extension(extension)
        print("Data updated : "+str(old_extension)+" -> "+str(extension))
    if extension == "Q" or extension == "q":
        encrypt_decrypt_folder()
    else :
        print("Extension is invalid (valid cataracts from a to z)")
        choice_private_key_path()
    

def encrypt_decrypt_folder(directory_path = find_folder_encrypt_path()):
    print("\n0    - First Time ?")
    print("1    - Encrypt Folder")
    print("2    - Decrypt Folder")
    print("99   - Reset")
    choice = input("Choice : ")
    if choice == "0":
        first_time()
    if choice == "1" :
        encrypt_folder(find_folder_encrypt_path())
    if choice == "2" :
        decrypt_folder(find_folder_encrypt_path())
    if choice == "3" :
        print("0    - Return")
        print("1    - Choice folder_encrypt_path")
        print("2    - Choice 'private_key_path'")
        print("3    - Choice extension")
        choice_settings = input("Choice : ")
        if choice_settings == "0" :
            encrypt_decrypt_folder()
        if choice_settings == "1" :
            choice_folder_encrypt_path()
        if choice_settings == "2" :
            choice_private_key_path()
        if choice_settings == "3" :
            choice_extension()
        else:
            encrypt_decrypt_folder()
    if choice == "99":
        reset_default_settings()
    else:
        encrypt_decrypt_folder()

if __name__ == "__main__":
    while True:
        encrypt_decrypt_folder()
