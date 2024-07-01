def drawUi(self, window:tk.Misc):

        self.chatDTO:ChatDTO = fetchAllTickets(self.application.user.token)
        
        sidebar_frame = tk.Frame(window, bg="#F5F5F5")
        sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Search bar
        search_entry = ttk.Entry(sidebar_frame, width=20)
        search_entry.pack(padx=10, pady=10)
        
        # Ticket list
        tickets = [
            {"icon": "🛠", "title": "Crash on load", "date": "Mar 3, 2023"},
            {"icon": "❌", "title": "User can't sign up", "date": "Jan 20, 2023"},
            {"icon": "🌑", "title": "Feature request: Dark mode", "date": "Dec 1, 2022"},
            {"icon": "🔒", "title": "Can't delete account", "date": "Nov 15, 2022"},
            {"icon": "💳", "title": "Billing issue", "date": "Nov 1, 2022"}
        ]

        for ticket in tickets:
            frame = tk.Frame(sidebar_frame, bg="#F5F5F5")
            frame.pack(fill=tk.X, pady=5)
            label_icon = tk.Label(frame, text=ticket["icon"], bg="#F5F5F5", font=("Arial", 12))
            label_icon.pack(side=tk.LEFT, padx=5)
            label_text = tk.Label(frame, text=f"{ticket['title']}\n{ticket['date']}", bg="#F5F5F5", font=("Arial", 10))
            label_text.pack(side=tk.LEFT)

        # Main Content Frame
        content_frame = tk.Frame(window)
        content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Ticket Title
        title_label = tk.Label(content_frame, text="User can't sign up", font=("Arial", 16, "bold"))
        title_label.pack(anchor=tk.W)

        # Status Section
        status_frame = tk.Frame(content_frame)
        status_frame.pack(anchor=tk.W, pady=10)
        status_label = tk.Label(status_frame, text="Status:", font=("Arial", 12, "bold"))
        status_label.pack(side=tk.LEFT)
        status_value = tk.Label(status_frame, text="Open", font=("Arial", 12))
        status_value.pack(side=tk.LEFT)

        # Details Section
        details_frame = tk.Frame(content_frame)
        details_frame.pack(anchor=tk.W, pady=10)
        details = [
            ("Reported by", "David Smith"),
            ("Reported on", "Mar 3, 2023"),
            ("Last updated by", "David Smith"),
            ("Last updated on", "Mar 3, 2023"),
            ("Priority", "High")
        ]

        for label_text, value_text in details:
            detail_frame = tk.Frame(details_frame)
            detail_frame.pack(anchor=tk.W, pady=2)
            label = tk.Label(detail_frame, text=f"{label_text}:", font=("Arial", 12, "bold"))
            label.pack(side=tk.LEFT)
            value = tk.Label(detail_frame, text=value_text, font=("Arial", 12))
            value.pack(side=tk.LEFT)

        # Assignee Section
        assignee_frame = tk.Frame(content_frame)
        assignee_frame.pack(anchor=tk.W, pady=10)
        assignee_label = tk.Label(assignee_frame, text="Assignee:", font=("Arial", 12, "bold"))
        assignee_label.pack(side=tk.LEFT)
        assignee_value = tk.Label(assignee_frame, text="Unassigned", font=("Arial", 12))
        assignee_value.pack(side=tk.LEFT)

        # Chat Section
        chat_frame = tk.Frame(content_frame)
        chat_frame.pack(anchor=tk.W, pady=10, fill=tk.BOTH, expand=True)
        
        chat_history = tk.Text(chat_frame, height=10, width=50, state=tk.DISABLED)
        chat_history.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        chat_scroll = tk.Scrollbar(chat_frame, command=chat_history.yview)
        chat_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        chat_history['yscrollcommand'] = chat_scroll.set

        chat_entry = tk.Entry(content_frame, width=50)
        chat_entry.pack(pady=10)

        def send_message(event=None):
            message = chat_entry.get()
            if message:
                chat_history.config(state=tk.NORMAL)
                chat_history.insert(tk.END, "You: " + message + "\n")
                chat_history.config(state=tk.DISABLED)
                chat_entry.delete(0, tk.END)

        chat_entry.bind("<Return>", send_message)

        send_button = tk.Button(content_frame, text="Send", command=send_message)
        send_button.pack()

        # -- Dev -- #

        for chat in self.chatDTO["chat"]:
            self.listBox.insert(tk.END, f'{chat["ticket"]["description"]} - {chat["ticket"]["state"]}')