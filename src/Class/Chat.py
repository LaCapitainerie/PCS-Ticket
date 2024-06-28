from uuid import UUID
from Class.Ticket import Ticket
from Class.User import User
from Class.Message import Message

# -- Class Chat -- #

class Chat:

    # -- Constructor -- #

    def __init__(self, chat):
        self.id:UUID = chat["id"]
        self.view:bool = chat["view"]
        self.ticket = Ticket(chat["ticket"])
        self.userId = [User(user) for user in chat["userId"]]
        self.message = [Message(message) for message in chat["message"]]

# -- ChatDTO Class -- #

class ChatDTO(dict):
    chat:list[Chat]