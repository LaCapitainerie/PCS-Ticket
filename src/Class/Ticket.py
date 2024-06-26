from typing import Literal
from uuid import UUID
from requests import Timeout, RequestException, get, exceptions

from Class.User import User
import constants

# -- Ticket Class -- #

class Ticket(dict):

    # -- Attributes -- #

    id:UUID
    type:str
    state:Literal['Backlog', 'Ready', 'In progress', 'Done']
    description:str
    chat_id:UUID

    # -- Constructor -- #

    def __init__(self, ticket):
        self.update(ticket)

# -- Fetch all tickets -- #

def fetchAllTickets(usertoken:str) -> list[Ticket]:
    try:
        #usertoken = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpZFVzZXIiOiIxMjNlNDU2Ny1lODliLTEyZDMtYTQ1Ni00MjYyMTQxNzQwMDAiLCJleHAiOjE3NTAzMzI4MDl9.FShzAVpmmEOTSfvL1NyQWjfzIP48EOM-qjuumeMAbkJz_gnYYHEnc3gyNC-8PQdtaAN-TnM2tTtJviD_4oeCZw"

        response = get(
            constants.API_URL + "/administration/ticket",
            headers={"Authorization": usertoken}
        )

        response.raise_for_status()

        return response.json()["chat"]

    except exceptions.HTTPError as http_err:
        print("HTTP Error:", http_err)
    except ConnectionError as conn_err:
        print("Erreur de connexion")
    except Timeout as timeout_err:
        print("Délai d'attente dépassé")
    except RequestException as req_err:
        print("Une erreur s'est produite lors de la requête")
    finally:
        return []