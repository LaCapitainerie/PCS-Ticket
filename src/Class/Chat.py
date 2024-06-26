from Class.Ticket import Ticket
from Class.User import User
from Class.Message import Message

# -- Class Chat -- #

class Chat(dict):

    # -- Attributes -- #

    id: str
    view: bool
    ticket: Ticket
    userId: list[User]
    message: list[Message]

    # -- Constructor -- #

    def __init__(self, chat):
        self.update(chat)

    # -- UI -- #

    def drawUi(self):
        pass