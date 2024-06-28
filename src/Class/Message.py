from typing import Literal
from uuid import UUID

# -- Message Class -- #

class Message:

    # -- Constructor -- #

    def __init__(self, message):
        self.id:UUID = message["id"]
        self.content:str = message["content"]
        self.date:str = message["date"]
        self.type:Literal["paiement"] = message["type"]
        self.userId:UUID = message["userId"]
        self.chatId:UUID = message["chatId"]