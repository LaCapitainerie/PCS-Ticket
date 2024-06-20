import tkinter as tk

from src.Dashboard import Dashboard
from src.Login import Login
from src.State import State
from src.Tickets import Tickets


class Application:
    def __init__(self):
        self.currentUser = None
        self.window = tk.Tk()
        self.window.title("Paris Caretaker Service - Ticket")
        self.window.configure(bg='black')
        self.window.state('zoomed')
        self.state = State.LOGIN

        self.login = Login(self.window, self)
        self.dashboard = Dashboard(self.window, self)
        self.tickets = Tickets(self.currentUser)
        self.login.drawUi()

        self.window.mainloop()

    def clearAll(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def onLoginSuccess(self, user):
        self.currentUser = user
        self.state = State.DASHBOARD
        self.clearAll()
        self.dashboard.drawUi(self.tickets)
