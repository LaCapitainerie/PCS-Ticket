import select
import tkinter as tk
from tkinter import Tk, ttk
import requests

# Mock function to replace fetchAllTickets
def fetchAllTickets(usertoken: str):
    return {
        "chat": [
            {
                "id": "e02934d9-cb1b-475f-9972-90816d402518",
                "view": False,  # type: ignore
                "ticket": {
                    "id": "123e4567-e89b-12d3-a486-426614174001",
                    "type": "paiement",
                    "state": "progress",
                    "description": "Problème avec le serveur",
                    "chatId": "e02934d9-cb1b-475f-9972-90816d402518"
                },
                "userId": [
                    {
                        "id": "123e4567-e89b-12d3-a456-426214174000",
                        "type": "admin",
                        "mail": "admin@gmail.com",
                        "password": "",
                        "registerDate": "2024-06-18T01:44:57.071232+02:00",
                        "lastConnectionDate": "2024-06-28T12:24:41.684531+02:00",
                        "avatar": "oui.png",
                        "site": "Paris",
                        "description": "Premier administrateur !",
                        "firstName": "",
                        "lastName": "",
                        "phoneNumber": "0669902851",
                        "nickname": "administrateur",
                        "token": ""
                    },
                    {
                        "id": "5fb3b5ce-84e1-43f0-890f-3632dbb2d741",
                        "type": "provider",
                        "mail": "kerian.bourdin@outlook.com",
                        "password": "",
                        "registerDate": "2024-06-07T03:00:07.866755+02:00",
                        "lastConnectionDate": "2024-06-20T11:00:40.01206+02:00",
                        "avatar": "",
                        "site": "",
                        "description": "",
                        "firstName": "",
                        "lastName": "",
                        "phoneNumber": "0629240719",
                        "nickname": "",
                        "token": ""
                    }
                ],
                "message": [
                    {
                        "id": "123e4567-e89b-98d3-a456-426614174002",
                        "content": "Bonjour, je voulais savoir si vous acceptez paypal ?",
                        "date": "2024-06-20T04:11:00.597749Z",
                        "type": "text",
                        "userId": "5fb3b5ce-84e1-43f0-890f-3632dbb2d741",
                        "chatId": "e02934d9-cb1b-475f-9972-90816d402518"
                    }
                ]
            }
        ]
    }

def dashboard_ui(root: Tk, token: str = "", our_user: dict = {}):
    root.state('zoomed')

    admintoken = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpZFVzZXIiOiIxMjNlNDU2Ny1lODliLTEyZDMtYTQ1Ni00MjYyMTQxNzQwMDAiLCJleHAiOjE3NTAzMzI4MDl9.FShzAVpmmEOTSfvL1NyQWjfzIP48EOM-qjuumeMAbkJz_gnYYHEnc3gyNC-8PQdtaAN-TnM2tTtJviD_4oeCZw"

    # Fetch tickets using the provided token (example implementation)
    tickets = fetchAllTickets(
        admintoken
    ).get("chat", [])

    # Main UI code as defined before
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Left Sidebar Frame
    sidebar_frame = tk.Frame(main_frame, bg="#F5F5F5")
    sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

    # Search bar
    search_entry = ttk.Entry(sidebar_frame, width=50)
    search_entry.pack(padx=10, pady=10)

    # Listbox for tickets
    ticket_listbox = tk.Listbox(sidebar_frame)
    ticket_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Main Content Frame
    content_frame = tk.Frame(main_frame)
    content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

    title_label = tk.Label(content_frame, text="", font=("Arial", 16, "bold"))
    title_label.pack(anchor=tk.W)

    status_frame = tk.Frame(content_frame)
    status_frame.pack(anchor=tk.W, pady=10)
    status_label = tk.Label(status_frame, text="Status:", font=("Arial", 12, "bold"))
    status_label.pack(side=tk.LEFT)
    status_value = tk.Label(status_frame, text="", font=("Arial", 12))
    status_value.pack(side=tk.LEFT)

    details_frame = tk.Frame(content_frame)
    details_frame.pack(anchor=tk.W, pady=10)

    assignee_frame = tk.Frame(content_frame)
    assignee_frame.pack(anchor=tk.W, pady=10)
    assignee_label = tk.Label(assignee_frame, text="Assignee:", font=("Arial", 12, "bold"))
    assignee_label.pack(side=tk.LEFT)
    assignee_value = tk.Label(assignee_frame, text="Unassigned", font=("Arial", 12))
    assignee_value.pack(side=tk.LEFT)

    chat_frame = tk.Frame(content_frame)
    chat_frame.pack(anchor=tk.W, pady=10, fill=tk.BOTH, expand=True)

    chat_history = tk.Text(chat_frame, height=10, width=50, state=tk.DISABLED)
    chat_history.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    chat_scroll = tk.Scrollbar(chat_frame, command=chat_history.yview)
    chat_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    chat_history['yscrollcommand'] = chat_scroll.set

    chat_entry = tk.Entry(content_frame, width=50)
    chat_entry.pack(pady=10)

    global selected_ticket
    selected_ticket = {}

    def fetch_message(event=None):
        chat_history.config(state=tk.NORMAL)
        chat_history.delete("1.0", tk.END)

        r = requests.get(
            'http://localhost:8080/api/chat/' + tickets[ticket_listbox.curselection()[0]]["id"],
            headers={
                "Authorization": admintoken,
            }
        )

        for message in r.json()["chat"]["message"]:
            chat_history.insert(tk.END, f'{message["userId"]}: {message["content"]}\n')

        chat_history.config(state=tk.DISABLED)


    def send_message(event=None):
        message = chat_entry.get()

        if message:

            r = requests.post(
                'http://localhost:8080/api/chat',
                headers={
                    "Authorization": token,
                },
                json={
                    "userId": [
                        tickets[ticket_listbox.curselection()[0]]["userId"][0],
                        tickets[ticket_listbox.curselection()[0]]["userId"][1]
                    ],
                    "message": [
                        {
                            "content": message,
                            "type": "text"
                        }
                    ]
                }
            )

            fetch_message()

    chat_entry.bind("<Return>", send_message)

    send_button = tk.Button(content_frame, text="Send", command=send_message)
    send_button.pack()

    def display_ticket_details(ticket):
        title_label.config(text=f'{ticket["ticket"]["type"]} {ticket["ticket"]["state"]}')
        status_value.config(text="Open")

        for widget in details_frame.winfo_children():
            widget.destroy()

        for label_text, value_text in ticket["ticket"].items():
            detail_frame = tk.Frame(details_frame)
            detail_frame.pack(anchor=tk.W, pady=2)
            label = tk.Label(detail_frame, text=f"{label_text}:", font=("Arial", 12, "bold"))
            label.pack(side=tk.LEFT)
            value = tk.Label(detail_frame, text=value_text, font=("Arial", 12))
            value.pack(side=tk.LEFT)

        fetch_message()

    # Populate Listbox with tickets
    for index, ticket in enumerate(tickets):
        ticket_listbox.insert(index, f'{ticket["ticket"]["description"]} ({ticket["ticket"]["state"]})')

    def on_ticket_select(event):
        selected_index = ticket_listbox.curselection()
        if selected_index:
            selected_ticket = tickets[selected_index[0]]
            display_ticket_details(selected_ticket)

    ticket_listbox.bind("<<ListboxSelect>>", on_ticket_select)

    return main_frame