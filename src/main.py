from tkinter import Tk
from Dashboard import dashboard_ui
from Login import login_ui

window = Tk()
window.title("Paris Caretaker Service - Ticket")
window.configure(bg='#F0F0F0')
window.state('zoomed')

user = {'id': 'f14efbc8-c240-4774-9782-f4520039db60', 'type': 'lessor', 'mail': 'hugo.antreassian@gmail.com', 'password': '', 'registerDate': '2024-07-10T17:38:24.9045Z', 'lastConnectionDate': '2024-07-10T17:38:24.9045Z', 'avatar': '', 'site': '', 'description': '', 'firstName': 'Hugo', 'lastName': 'Antreassian', 'phoneNumber': '06 23 00 01 48', 'nickname': '', 'token': 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpZFVzZXIiOiJmMTRlZmJjOC1jMjQwLTQ3NzQtOTc4Mi1mNDUyMDAzOWRiNjAiLCJleHAiOjE3NTIxNzkzNTV9.-vdAFHiKL4J5CwqxbQmL8zEVTbt-hMEEJBitAWTHcr3TMbY3OOtjC2dFwsZ2jXu9E9qUvkY9MmxIsz3lthTdFg'}
#login_ui(window)
dashboard_ui(window, user)

window.mainloop()