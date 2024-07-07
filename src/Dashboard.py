import tkinter as tk
from tkinter import Tk, ttk
from turtle import st
import requests

# Mock function to replace fetchAllTickets
def fetchAllTickets(usertoken: str):

    r = requests.get(
        'http://77.237.246.8:8080/api/ticket',
        headers={
            "Authorization": usertoken,
        }
    )

    if r.status_code != 200:
        return {}

    return r.json()

def dashboard_ui(root: Tk, our_user: dict = {}):
    root.state('zoomed')

    admintoken = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpZFVzZXIiOiIxMjNlNDU2Ny1lODliLTEyZDMtYTQ1Ni00MjYyMTQxNzQwMDAiLCJleHAiOjE3NTAzMzI4MDl9.FShzAVpmmEOTSfvL1NyQWjfzIP48EOM-qjuumeMAbkJz_gnYYHEnc3gyNC-8PQdtaAN-TnM2tTtJviD_4oeCZw"

    # Fetch tickets using the provided token (example implementation)
    tickets = fetchAllTickets(admintoken).get("chat", [])

    # Main UI code as defined before
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Top Frame for deconnexion button
    top_frame = tk.Frame(root)
    top_frame.pack(side=tk.TOP, fill=tk.X)
    
    # Logged in as label
    logged_in_label = tk.Label(top_frame, text=f"Logged in as {our_user.get('mail')}", font=("Arial", 12))
    logged_in_label.pack(side=tk.LEFT, padx=10, pady=10)

    deconnexion_button = tk.Button(top_frame, text="Deconnexion", command=root.destroy)
    deconnexion_button.pack(side=tk.RIGHT, padx=10, pady=10)

    # Left Sidebar Frame
    sidebar_frame = tk.Frame(main_frame, bg="#F5F5F5")
    sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

    # Search bar
    search_entry = ttk.Entry(sidebar_frame, width=50)
    search_entry.pack(padx=10, pady=10)

    # Dropdown list for state filter
    state_filter = ttk.Combobox(sidebar_frame, values=["All", "progress", "open", "closed"])
    state_filter.current(0)
    state_filter.pack(padx=10, pady=10)

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


    # -- Input fields for ticket details { "id", "type", "state", "description", "chatId" }-- #

    id_detail_frame = tk.Frame(details_frame)
    id_detail_frame.pack(anchor=tk.W, pady=2)
    id_label = tk.Label(id_detail_frame, text="id:", font=("Arial", 12, "bold"))
    id_label.pack(side=tk.LEFT)

    id_value = tk.Entry(id_detail_frame, width=50)
    id_value.pack(side=tk.LEFT)


    type_detail_frame = tk.Frame(details_frame)
    type_detail_frame.pack(anchor=tk.W, pady=2)
    type_label = tk.Label(type_detail_frame, text="type:", font=("Arial", 12, "bold"))
    type_label.pack(side=tk.LEFT)

    type_value = tk.Entry(type_detail_frame, width=50)
    type_value.pack(side=tk.LEFT)


    state_detail_frame = tk.Frame(details_frame)
    state_detail_frame.pack(anchor=tk.W, pady=2)
    state_label = tk.Label(state_detail_frame, text="state:", font=("Arial", 12, "bold"))
    state_label.pack(side=tk.LEFT)

    state_value = tk.Entry(state_detail_frame, width=50)
    state_value.pack(side=tk.LEFT)


    description_detail_frame = tk.Frame(details_frame)
    description_detail_frame.pack(anchor=tk.W, pady=2)
    description_label = tk.Label(description_detail_frame, text="description:", font=("Arial", 12, "bold"))
    description_label.pack(side=tk.LEFT)
    
    description_value = tk.Entry(description_detail_frame, width=50)
    description_value.pack(side=tk.LEFT)


    chatId_detail_frame = tk.Frame(details_frame)
    chatId_detail_frame.pack(anchor=tk.W, pady=2)
    chatId_label = tk.Label(chatId_detail_frame, text="chatId:", font=("Arial", 12, "bold"))
    chatId_label.pack(side=tk.LEFT)

    chatId_value = tk.Entry(chatId_detail_frame, width=50)
    chatId_value.pack(side=tk.LEFT)

    global selected_ticket
    selected_ticket = {}

    def fetch_message(event=None):
        chat_history.config(state=tk.NORMAL)
        chat_history.delete("1.0", tk.END)

        r = requests.get(
            'http://77.237.246.8:8080/api/chat/' + tickets[ticket_listbox.curselection()[0]]["id"],
            headers={
                "Authorization": admintoken,
            }
        )

        print("retreiving messages", r.json())

        for message in r.json()["chat"]["message"]:
            chat_history.insert(tk.END, f'{message["userId"]}: {message["content"]}\n')

        chat_history.config(state=tk.DISABLED)

    def send_message(event=None):
        message = chat_entry.get()

        if message:
            r = requests.post(
                'http://77.237.246.8:8080/api/chat',
                headers={
                    "Authorization": our_user.get("token"),
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


    def save_ticket():
        print("Saving ticket")

        returnTicket = {
            "id": id_value.get(),
            "type": type_value.get(),
            "state": state_value.get(),
            "description": description_value.get(),
            "chatId": chatId_value.get()
        }

        print(returnTicket)

        r = requests.put(
                'http://localhost:8080/api/ticket/' + id_value.get(),
                headers={
                    "Authorization": our_user.get("token"),
                },
                json=returnTicket
            )
        
        if r.status_code == 200:
            print("Ticket updated")

            fetchAllTickets(admintoken)

    # Save button
    save_button = tk.Button(details_frame, text="Save", command=save_ticket)
    save_button.pack(pady=10)
    

    def display_ticket_details(ticket):
        title_label.config(text=f'{ticket["ticket"]["type"]} {ticket["ticket"]["state"]}')
        status_value.config(text="Open")

        # Clear existing value in the entry widget before inserting new value
        id_value.delete(0, tk.END)
        id_value.insert(tk.END, ticket["ticket"].get("id", "N/A"))

        type_value.delete(0, tk.END)
        type_value.insert(tk.END, ticket["ticket"].get("type", "N/A"))

        state_value.delete(0, tk.END)
        state_value.insert(tk.END, ticket["ticket"].get("state", "N/A"))

        description_value.delete(0, tk.END)
        description_value.insert(tk.END, ticket["ticket"].get("description", "N/A"))

        chatId_value.delete(0, tk.END)
        chatId_value.insert(tk.END, ticket["ticket"].get("chatId", "N/A"))

        fetch_message()

    def populate_listbox():
        ticket_listbox.delete(0, tk.END)
        for index, ticket in enumerate(filtered_tickets()):
            ticket_listbox.insert(index, f'{ticket["ticket"]["description"]} ({ticket["ticket"]["state"]})')

    def filtered_tickets():
        search_text = search_entry.get().lower()
        state_text = state_filter.get().lower()
        return [
            ticket for ticket in tickets
            if search_text in ticket["ticket"]["description"].lower() and
            (state_text == "all" or ticket["ticket"]["state"].lower() == state_text)
        ]

    def on_ticket_select(event):
        selected_index = ticket_listbox.curselection()
        if selected_index:
            selected_ticket = tickets[selected_index[0]]
            display_ticket_details(selected_ticket)

    search_entry.bind("<KeyRelease>", lambda event: populate_listbox())
    state_filter.bind("<<ComboboxSelected>>", lambda event: populate_listbox())

    populate_listbox()
    ticket_listbox.bind("<<ListboxSelect>>", on_ticket_select)

    return main_frame
