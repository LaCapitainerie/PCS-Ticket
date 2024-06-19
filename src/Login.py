import os
import tkinter as tk
from PIL import Image, ImageTk
from requests import RequestException, Timeout

import constants
import requests

from src.User import User


class Login:
    def __init__(self, window, app):
        self.errorLabel = None
        if not os.path.isfile(constants.LOGO_PATH):
            raise FileNotFoundError(f"File '{constants.LOGO_PATH}' not found")

        self.app = app
        self.window = window
        self.image = Image.open(constants.LOGO_PATH)
        self.imagetk = ImageTk.PhotoImage(self.image)
        self.labelImage = tk.Label(window, image=self.imagetk)
        self.labelImage.pack(side=tk.TOP, pady=10)

        self.labelEmail = tk.Label(window, text="Email :", fg="white", bg="black")
        self.labelEmail.pack(side=tk.TOP, pady=10)

        self.entryEmail = tk.Entry(window, width=40)
        self.entryEmail.pack()

        self.labelPassword = tk.Label(window, text="Mot de passe :", fg="white", bg="black")
        self.labelPassword.pack(side=tk.TOP, pady=10)

        self.entryPassword = tk.Entry(window, show="*", width=40)
        self.entryPassword.pack()

        self.button_login = tk.Button(window, text="Connexion", command=self.login)
        self.button_login.pack(side=tk.TOP, pady=10)

        self.errorLabel = tk.Label(window, text="", fg="red", bg="black")
        self.errorLabel.pack(side=tk.TOP, pady=10)

    def connexionError(self, error):
        self.errorLabel.config(text=error)

    def login(self):
        email = self.entryEmail.get()
        password = self.entryPassword.get()
        try:
            payload = {
                "mail": email,
                "password": password
            }
            response = requests.post(constants.API_URL + "/user/login", json=payload)
            response.raise_for_status()

            userJson = response.json()["user"]
            user = User(userJson["id"],
                        userJson["type"],
                        userJson["mail"],
                        userJson["password"],
                        userJson["registerDate"],
                        userJson["lastConnectionDate"],
                        userJson["avatar"],
                        userJson["site"],
                        userJson["description"],
                        userJson["firstName"],
                        userJson["lastName"],
                        userJson["token"])
            self.connexionError("")
            self.app.onLoginSuccess(user)
        except requests.exceptions.HTTPError as http_err:
            self.connexionError("Email ou mot de passe invalide.")
        except ConnectionError as conn_err:
            self.connexionError("Erreur de connexion")
        except Timeout as timeout_err:
            self.connexionError("Délai d'attente dépassé")
        except RequestException as req_err:
            self.connexionError("Une erreur s'est produite lors de la requête")

    def tkraise(self):
        pass

    def grid(self, row, column, sticky):
        pass
