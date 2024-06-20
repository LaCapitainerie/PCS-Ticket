import requests
from requests import Timeout, RequestException

from src import constants


class Tickets:
    def __init__(self, user):
        self.tickets = []
        self.user = user

    def fetchAllTickets(self):
        try:
            usertoken = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpZFVzZXIiOiIxMjNlNDU2Ny1lODliLTEyZDMtYTQ1Ni00MjYyMTQxNzQwMDAiLCJleHAiOjE3NTAzMzI4MDl9.FShzAVpmmEOTSfvL1NyQWjfzIP48EOM-qjuumeMAbkJz_gnYYHEnc3gyNC-8PQdtaAN-TnM2tTtJviD_4oeCZw"
            header = {
                "Authorization": usertoken
            }

            response = requests.get(constants.API_URL + "/administration/ticket", headers=header)
            self.tickets = response.json()["chat"]

            response.raise_for_status()

        except requests.exceptions.HTTPError as http_err:
            print("HTTP Error:", http_err)
        except ConnectionError as conn_err:
            print("Erreur de connexion")
        except Timeout as timeout_err:
            print("Délai d'attente dépassé")
        except RequestException as req_err:
            print("Une erreur s'est produite lors de la requête")