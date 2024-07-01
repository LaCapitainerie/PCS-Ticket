from tkinter import Tk
from Dashboard import dashboard_ui
from Login import login_ui

window = Tk()
window.title("Paris Caretaker Service - Ticket")
window.configure(bg='white')
window.state('zoomed')

usertoken = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpZFVzZXIiOiI5ODU3NTczYi00NDM4LTQ3MTQtYTIyYy04ZGEwNTcxMTZjOWYiLCJleHAiOjE3MjA0NjU1NDZ9.Lg1UpJZkAlggwJj9GH1vnaESqavTqH8uafRsURLSK5KDad-bWQeXxn-exx0EvhkkgeLVwx3EMUXOrfIGE_kKtQ"

login_ui(window)

window.mainloop()