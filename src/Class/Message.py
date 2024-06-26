from typing import Literal

# -- Message Class -- #

class Message(dict):

    # -- Attributes -- #

    id:str
    content:str
    date:str
    type:Literal['text', 'image']
    userId:str
    chatId:str

    # -- Constructor -- #

    def __init__(self, message):
        self.update(message)