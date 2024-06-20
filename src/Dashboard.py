import os
import tkinter as tk
from PIL import Image, ImageTk
from requests import RequestException, Timeout


class Dashboard(tk.Frame):
    def __init__(self, window, app):
        super().__init__(window)
        self.currentUser = None
        self.app = app
        self.window = window

        self.labelEmail = tk.Label(window, text="Email :", fg="white", bg="black")
        self.labelEmail.pack(side=tk.TOP, pady=10)
