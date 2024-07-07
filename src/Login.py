import tkinter as tk
from PIL import Image, ImageTk

from Dashboard import dashboard_ui
import requests


def login_ui(window:tk.Tk, user):
    window.state('zoomed')

    image = Image.open("./resources/logo.png")
    imagetk = ImageTk.PhotoImage(image)
    labelImage = tk.Label(window, image=imagetk) # type: ignore
    labelImage.pack(side=tk.TOP, pady=10)

    labelEmail = tk.Label(window, text="Email :", fg="#226D68")
    labelEmail.pack(side=tk.TOP, pady=10)

    entryEmail = tk.Entry(window, width=40)
    entryEmail.pack()

    labelPassword = tk.Label(window, text="Mot de passe :", fg="#226D68")
    labelPassword.pack(side=tk.TOP, pady=10)

    entryPassword = tk.Entry(window, show="*", width=40)
    entryPassword.pack()

    def login():
        email = entryEmail.get()
        password = entryPassword.get()

        try:
            payload = {
                "mail": email,
                "password": password
            }
            response = requests.post("http://77.237.246.8:8080/api" + "/user/login", json=payload)

            if response.status_code == 401:
                print(f"Accès non autorisé  {email} {password}")
                errorLabel.config(text="Accès non autorisé")
                raise Exception("Unauthorized")
            else:
                print(response.status_code)

            response.raise_for_status()  # Raise HTTPError for bad responses

            print(response.json().get("user", {}))

            # If login is successful, return the user object
            return response.json().get("user", {})

        except requests.exceptions.HTTPError:
            print(f"Email ou mot de passe invalide. {email} {password}")
        except requests.exceptions.ConnectionError:
            print("Erreur de connexion")
        except requests.exceptions.Timeout:
            print("Délai d'attente dépassé")
        except requests.exceptions.RequestException:
            print("Une erreur s'est produite lors de la requête")
        except Exception as e:
            print(e)

        return None

    button_login = tk.Button(window, text="Connexion", command=lambda: handle_login(window))
    button_login.pack(side=tk.TOP, pady=10)

    def handle_login(window: tk.Misc):
        user = login()
        if user:
            # Destroy the current login UI
            window.destroy()

            # Initialize the dashboard UI with the user token
            root = tk.Tk()
            root.title("Dashboard")
            dashboard_ui(root, user)  # Pass the user token to the dashboard UI
            root.mainloop()

        elif errorLabel.cget("text") == "":
            # Display login error message
            errorLabel.config(text="Email ou mot de passe invalide.")

    errorLabel = tk.Label(window, text="", fg="red")
    errorLabel.pack(side=tk.TOP, pady=10)
