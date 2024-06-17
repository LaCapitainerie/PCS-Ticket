import tkinter as tk
from src.Login import Login


class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Paris Caretaker Service - Ticket")
        self.window.configure(bg='black')
        self.window.state('zoomed')

        self.login = Login(self.window)

        self.window.mainloop()
