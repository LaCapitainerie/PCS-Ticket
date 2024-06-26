import tkinter as tk

from Class.User import User
from Dashboard import Dashboard
from Login import Login
from State import State
from Class.Ticket import Ticket, fetchAllTickets


class Application(dict):

    # -- Static Attributes -- #

    user: User
    tickets: list[Ticket]

    # -- Pages -- #
    
    login: Login
    dashboard: Dashboard

    state: State

    # -- Constructor -- #

    def __init__(self):
        self.currentUser:User

        # -- Create the login and dashboard objects -- #

        self.window = tk.Tk()
        self.window.title("Paris Caretaker Service - Ticket")
        self.window.configure(bg='white')
        self.window.state('zoomed')
        self.state = State.LOGIN



        self.login.drawUi()

        self.window.mainloop()

    def clearAll(self):
        for widget in self.window.winfo_children():
            widget.destroy()
