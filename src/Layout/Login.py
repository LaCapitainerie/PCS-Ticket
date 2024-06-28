import os
import tkinter as tk
from PIL import Image, ImageTk

import constants
import requests

from Class.User import User

class Login(tk.Frame):
    def __init__(self, window:tk.Misc, application):
        
        # -- Attributes -- #

        self.application = application

        super().__init__(window)
        self.button_login = None
        self.entryPassword = None
        self.labelPassword = None
        self.entryEmail = None
        self.labelEmail = None
        self.labelImage = None
        self.imagetk = None
        self.image = None
        self.errorLabel = None
        if not os.path.isfile(constants.LOGO_PATH):
            raise FileNotFoundError(f"File '{constants.LOGO_PATH}' not found")


    def drawUi(self, window:tk.Misc):
        self.image = Image.open(constants.LOGO_PATH)
        self.imagetk = ImageTk.PhotoImage(self.image)
        self.labelImage = tk.Label(window, image=self.imagetk) # type: ignore
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


    def login(self) -> User | None:

        # -- Dev -- #

        # user = User({"token": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpZFVzZXIiOiIxMjNlNDU2Ny1lODliLTEyZDMtYTQ1Ni00MjYyMTQxNzQwMDAiLCJleHAiOjE3NTAzMzI4MDl9.FShzAVpmmEOTSfvL1NyQWjfzIP48EOM-qjuumeMAbkJz_gnYYHEnc3gyNC-8PQdtaAN-TnM2tTtJviD_4oeCZw"})

        email = self.entryEmail.get() # type: ignore
        password = self.entryPassword.get() # type: ignore

        def connexionError(error):
            self.errorLabel.config(text=error) # type: ignore

        try:
            payload = {
                "mail": email,
                "password": password
            }
            response = requests.post(constants.API_URL + "/administration/login", json=payload)
            response.raise_for_status()

            userJson:User = User(response.json().get("user", {}))

            self.application.user = userJson

            self.application.drawDashboard()

        except requests.exceptions.HTTPError:
            connexionError("Email ou mot de passe invalide.")
        except requests.ConnectionError:
            connexionError("Erreur de connexion")
        except requests.Timeout:
            connexionError("Délai d'attente dépassé")
        except requests.RequestException:
            connexionError("Une erreur s'est produite lors de la requête")
        finally:
            return None
