import os
import tkinter as tk
from PIL import Image, ImageTk


class Login:
    def __init__(self, window):
        imagePath = "../resources/logo.png"
        if not os.path.isfile(imagePath):
            raise FileNotFoundError(f"File '{imagePath}' not found")

        self.image = Image.open(imagePath)
        self.imagetk = ImageTk.PhotoImage(self.image)
        self.labelImage = tk.Label(window, image=self.imagetk)
        self.labelImage.pack(side=tk.TOP, pady=10)

        labelEmail = tk.Label(window, text="Email :", fg="white", bg="black")
        labelEmail.pack(side=tk.TOP, pady=10)

        entryEmail = tk.Entry(window, width=40)
        entryEmail.pack()

        labelPassword = tk.Label(window, text="Mot de passe :", fg="white", bg="black")
        labelPassword.pack(side=tk.TOP, pady=10)

        entryPassword = tk.Entry(window, show="*", width=40)
        entryPassword.pack()

        button_login = tk.Button(window, text="Connexion", command=self.login)
        button_login.pack(side=tk.TOP, pady=10)

    def login(self):
        print("oui")
