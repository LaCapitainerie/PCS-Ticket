import tkinter as tk
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

        self.frames = {State.LOGIN: Login(self.window, self)}
        self.showFrame(State.LOGIN)

        self.window.mainloop()

    def onLoginSuccess(self, user):
        self.currentUser = user
        self.showFrame(State.DASHBOARD)

    def createFrame(self):
        self.frames[State.LOGIN] = Login(self.window, self)
        # self.frames[State.DASHBOARD] = Dashboard(self.window, self)

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def showFrame(self, state):
        self.state = state
        frame = self.frames[state]
        frame.tkraise()
