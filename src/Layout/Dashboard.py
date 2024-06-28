import tkinter as tk

from Class.Chat import ChatDTO

# -- Dashboard Class -- #

class Dashboard(tk.Frame):

    # -- Constructor -- #
    
    def __init__(self, window:tk.Misc, application):

        # -- Attributes -- #

        self.application = application

        super().__init__(window)
        self.listBox = None
        self.labelEmail = None
        self.currentUser = None


    def drawUi(self, window:tk.Misc):

		# -- Frame -- #

        self.chatDTO:ChatDTO = fetchAllTickets(self.application.user.token)
        
        frameListBox = tk.Frame(window)
        frameListBox.place(relwidth=0.25, relheight=1.0)
        
        self.label = tk.Label(frameListBox, text="Tickets", font=("Helvetica", 16)).pack(fill=tk.X)

        self.listBox = tk.Listbox(frameListBox, selectmode=tk.SINGLE)
        self.listBox.pack(fill=tk.BOTH, expand=True)

        for chat in self.chatDTO["chat"]:
            self.listBox.insert(tk.END, f'{chat["ticket"]["description"]} - {chat["ticket"]["state"]}')


def fetchAllTickets(usertoken:str) -> ChatDTO:

    # usertoken = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpZFVzZXIiOiIxMjNlNDU2Ny1lODliLTEyZDMtYTQ1Ni00MjYyMTQxNzQwMDAiLCJleHAiOjE3NTAzMzI4MDl9.FShzAVpmmEOTSfvL1NyQWjfzIP48EOM-qjuumeMAbkJz_gnYYHEnc3gyNC-8PQdtaAN-TnM2tTtJviD_4oeCZw"
    
    # header = {
    #     "Authorization": usertoken
    # }

    # response = requests.get(constants.API_URL + "/administration/ticket", headers=header)
    
    return {
	"chat": [
		{
			"id": "e02934d9-cb1b-475f-9972-90816d402518",
			"view": False, # type: ignore
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
