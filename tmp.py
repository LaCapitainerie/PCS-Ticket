import tkinter as tk
from tkinter import ttk

# Sample data for tickets
tickets = [
    {"icon": "🛠", "title": "Crash on load", "date": "Mar 3, 2023", "details": {"Reported by": "David Smith", "Reported on": "Mar 3, 2023", "Last updated by": "David Smith", "Last updated on": "Mar 3, 2023", "Priority": "High"}},
    {"icon": "❌", "title": "User can't sign up", "date": "Jan 20, 2023", "details": {"Reported by": "John Doe", "Reported on": "Jan 20, 2023", "Last updated by": "John Doe", "Last updated on": "Jan 20, 2023", "Priority": "High"}},
    {"icon": "🌑", "title": "Feature request: Dark mode", "date": "Dec 1, 2022", "details": {"Reported by": "Jane Smith", "Reported on": "Dec 1, 2022", "Last updated by": "Jane Smith", "Last updated on": "Dec 1, 2022", "Priority": "Medium"}},
    {"icon": "🔒", "title": "Can't delete account", "date": "Nov 15, 2022", "details": {"Reported by": "Bob Brown", "Reported on": "Nov 15, 2022", "Last updated by": "Bob Brown", "Last updated on": "Nov 15, 2022", "Priority": "Low"}},
    {"icon": "💳", "title": "Billing issue", "date": "Nov 1, 2022", "details": {"Reported by": "Alice Green", "Reported on": "Nov 1, 2022", "Last updated by": "Alice Green", "Last updated on": "Nov 1, 2022", "Priority": "High"}}
]

def create_main_ui(root):
    # Main UI code as defined before
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Left Sidebar Frame
    sidebar_frame = tk.Frame(main_frame, bg="#F5F5F5")
    sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

    # Search bar
    search_entry = ttk.Entry(sidebar_frame, width=20)
    search_entry.pack(padx=10, pady=10)

    ticket_list_frame = tk.Frame(sidebar_frame, bg="#F5F5F5")
    ticket_list_frame.pack(fill=tk.BOTH, expand=True)

    ticket_canvas = tk.Canvas(ticket_list_frame, bg="#F5F5F5")
    ticket_scrollbar = tk.Scrollbar(ticket_list_frame, orient="vertical", command=ticket_canvas.yview)
    ticket_scrollable_frame = tk.Frame(ticket_canvas, bg="#F5F5F5")

    ticket_scrollable_frame.bind(
        "<Configure>",
        lambda e: ticket_canvas.configure(
            scrollregion=ticket_canvas.bbox("all")
        )
    )

    ticket_canvas.create_window((0, 0), window=ticket_scrollable_frame, anchor="nw")
    ticket_canvas.configure(yscrollcommand=ticket_scrollbar.set)

    ticket_canvas.pack(side="left", fill="both", expand=True)
    ticket_scrollbar.pack(side="right", fill="y")

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

    def display_ticket_details(ticket):

        title_label.config(text=ticket["title"])
        status_value.config(text="Open")

        for widget in details_frame.winfo_children():
            widget.destroy()

        for label_text, value_text in ticket["details"].items():
            detail_frame = tk.Frame(details_frame)
            detail_frame.pack(anchor=tk.W, pady=2)
            label = tk.Label(detail_frame, text=f"{label_text}:", font=("Arial", 12, "bold"))
            label.pack(side=tk.LEFT)
            value = tk.Label(detail_frame, text=value_text, font=("Arial", 12))
            value.pack(side=tk.LEFT)

    # Populate ticket list
    for ticket in tickets:
        frame = tk.Frame(ticket_scrollable_frame, bg="#F5F5F5")
        frame.pack(fill=tk.X, pady=5)
        label_icon = tk.Label(frame, text=ticket["icon"], bg="#F5F5F5", font=("Arial", 12))
        label_icon.pack(side=tk.LEFT, padx=5)
        label_text = tk.Label(frame, text=f"{ticket['title']}\n{ticket['date']}", bg="#F5F5F5", font=("Arial", 10))
        label_text.pack(side=tk.LEFT)

        frame.bind("<Button-1>", lambda e, t=ticket: display_ticket_details(t))

    return main_frame


def main():
    root = tk.Tk()
    root.title("Ticket Tracker")

    main_frame = create_main_ui(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
