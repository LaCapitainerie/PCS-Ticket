import tkinter as tk

from Class.User import User
from Layout.Dashboard import Dashboard
from Layout.Login import Login
from constants import State
from Class.Ticket import Ticket


class Application(dict):

    # -- Constructor -- #

    def __init__(self):

        # -- Static Attributes -- #

        self.user: User
        self.tickets: list[Ticket]

        # -- Pages -- #
        
        self.login: Login
        self.dashboard: Dashboard

        self.state: State

        # -- Create the login and dashboard objects -- #

        self.window = tk.Tk()
        self.window.title("Paris Caretaker Service - Ticket")
        self.window.configure(bg='white')
        self.window.state('zoomed')
        self.state = State.LOGIN

        self.login = Login(self.window, self)
        self.dashboard = Dashboard(self.window, self)

        # -- Draw the login page -- #

        self.drawLogin()

        # -- Mainloop -- #

        self.window.mainloop()

    def clearAll(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def drawLogin(self):
        self.clearAll()
        self.login.drawUi(window=self.window)
        self.state = State.LOGIN

    def drawDashboard(self):
        self.clearAll()
        self.dashboard.drawUi(window=self.window)
        self.state = State.DASHBOARD





if __name__ == "__main__":
    Application()