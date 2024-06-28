from typing import Literal
from uuid import UUID

# -- User Class -- #

class User:

    # -- Constructor -- #

    def __init__(self, user):
        self.id:UUID = user.get("id", "")
        self.type:Literal['traveler', 'provider', 'lessor', 'admin'] = user.get("type", "")
        self.mail:str = user.get("mail", "")
        self.password:str = user.get("password", "")
        self.registerdate:str = user.get("registerdate", "")
        self.lastConnectionDate:str = user.get("lastConnectionDate", "")
        self.avatar:str = user.get("avatar", "")
        self.description:str = user.get("description", "")
        self.firstName:str = user.get("firstName", "")
        self.lastName:str = user.get("lastName", "")
        self.nickname:str = user.get("nickname", "")
        self.phoneNumber:str = user.get("phoneNumber", "")
        self.token:str = user.get("token", "")