from typing import Literal
from uuid import UUID

# -- Ticket Class -- #

class Ticket:

    # -- Constructor -- #

    def __init__(self, ticket):
        self.id:UUID = ticket["id"]
        self.type:str = ticket["type"]
        self.state:Literal['Backlog', 'Ready', 'In progress', 'Done'] = ticket["state"]
        self.description:str = ticket["description"]
        self.chat_id:UUID = ticket["chat_id"]