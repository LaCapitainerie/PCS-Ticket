
from typing import Literal

# -- User Class -- #

class User(dict):

    # -- Attributes -- #

    id:str
    type:Literal['traveler', 'provider', 'lessor', 'admin']
    mail:str
    password:str
    registerdate:str
    lastConnectionDate:str
    avatar:str
    description:str
    firstName:str
    lastName:str
    nickname:str
    phoneNumber:str
    token:str

    # -- Constructor -- #

    def __init__(self, user:'User'):
        self.update(user)

    # -- UI -- #

    def drawUi(self):
        pass