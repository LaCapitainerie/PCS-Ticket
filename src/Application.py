import tkinter as tk

from src.Dashboard import Dashboard
from src.Login import Login
from src.State import State


class Application:
    def __init__(self):
        self.currentUser = None
        self.window = tk.Tk()
        self.window.title("Paris Caretaker Service - Ticket")
        self.window.configure(bg='black')
        self.window.state('zoomed')
        self.state = State.LOGIN

        self.login = Login(self.window, self)

        self.clearAll()

        self.window.mainloop()

    def clearAll(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def onLoginSuccess(self, user):
        self.currentUser = user
