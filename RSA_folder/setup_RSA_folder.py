# commande à taper en ligne de commande après la sauvegarde de ce fichier:
# python setup.py build

from cx_Freeze import setup, Executable
  
executables = [
        Executable(script = "RSA Encrypt Decrypt.py",icon = "pop_art.ico")
]
# ne pas mettre "base = ..." si le programme n'est pas en mode graphique, comme c'est le cas pour chiffrement.py.
'''
buildOptions = dict( 
        includes = ["module1","module2","module3",...],
        include_files = ["fichier1.txt", "mon_icone.ico"]
)'''

setup(
        name = "RSA Encrypt Decrypt",
        version = "1.0",
        description = "RSA Encrypt and Decrypt",
        author = "TitouEntreprise",
        #options = dict(build_exe = buildOptions),
        executables = executables
)