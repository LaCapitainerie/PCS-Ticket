import os
import tkinter as tk
from PIL import Image, ImageTk
from requests import RequestException, Timeout

from Class.Ticket import Ticket, fetchAllTickets


class Dashboard(tk.Frame):
    def __init__(self, window, app):
        super().__init__(window)
        self.listBox = None
        self.labelEmail = None
        self.currentUser = None
        self.app = app
        self.window = window

    def drawUi(self, tickets:list[Ticket]):
        
        frameListBox = tk.Frame(self.window)
        frameListBox.place(relwidth=0.25, relheight=1.0)

        self.listBox = tk.Listbox(frameListBox, selectmode=tk.SINGLE)
        self.listBox.pack(fill=tk.BOTH, expand=True)
        for ticket in tickets:
            self.listBox.insert(tk.END, f'{ticket["ticket"]["description"]} - {ticket["ticket"]["state"]}')