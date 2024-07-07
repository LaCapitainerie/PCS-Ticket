from tkinter import Tk
from Dashboard import dashboard_ui
from Login import login_ui

window = Tk()
window.title("Paris Caretaker Service - Ticket")
window.configure(bg='#F0F0F0')
window.state('zoomed')

usertoken = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpZFVzZXIiOiI5ODU3NTczYi00NDM4LTQ3MTQtYTIyYy04ZGEwNTcxMTZjOWYiLCJleHAiOjE3MjA0NjU1NDZ9.Lg1UpJZkAlggwJj9GH1vnaESqavTqH8uafRsURLSK5KDad-bWQeXxn-exx0EvhkkgeLVwx3EMUXOrfIGE_kKtQ"

user = {'id': '6930e6ec-758c-48e0-815e-d24b2ae6f9ce', 'type': 'lessor', 'mail': 'lessor@gmail.com', 'password': '', 'registerDate': '2024-07-02T14:58:37.609712+02:00', 'lastConnectionDate': '2024-07-04T20:32:00.107468+02:00', 'avatar': 'https://th.bing.com/th/id/OIP.uEi-BYi_M-Rnv9abB82xqwHaHa?rs=1&pid=ImgDetMain', 'site': '', 'description': '', 'firstName': 'Thomas', 'lastName': 'Poupard', 'phoneNumber': '06 29 24 07 06', 'nickname': '', 'token': 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpZFVzZXIiOiI2OTMwZTZlYy03NThjLTQ4ZTAtODE1ZS1kMjRiMmFlNmY5Y2UiLCJleHAiOjE3NTE4Nzc5MTB9.b24X5A_hqlLG3DX7Pzpa_6NBu5Fp6cyPF0Vu-EKM8SYiludDdHA0EiY9OscF4ncL8k5B7BygG1QuwXvbiyw2rQ'}

dashboard_ui(window, user)

window.mainloop()