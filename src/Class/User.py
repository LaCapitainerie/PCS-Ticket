from typing import Literal
from uuid import UUID

# -- User Class -- #

class User:

    # -- Constructor -- #

    def __init__(self, user):
        self.id:UUID = user["id"]
        self.type:Literal['traveler', 'provider', 'lessor', 'admin'] = user["type"]
        self.mail:str = user["mail"]
        self.password:str = user["password"]
        self.registerdate:str = user["registerdate"]
        self.lastConnectionDate:str = user["lastConnectionDate"]
        self.avatar:str = user["avatar"]
        self.description:str = user["description"]
        self.firstName:str = user["firstName"]
        self.lastName:str = user["lastName"]
        self.nickname:str = user["nickname"]
        self.phoneNumber:str = user["phoneNumber"]
        self.token:str = user["token"]