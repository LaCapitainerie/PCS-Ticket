class User:
    def __init__(self,
                 id: str,
                 type: str,
                 mail: str,
                 password: str,
                 registerDate: str,
                 lastConnectionDate: str,
                 avatar: str,
                 site: str,
                 description: str,
                 firstName: str,
                 lastName: str,
                 token: str):
        self.id = id
        self.type = type
        self.email = mail
        self.password = password
        self.registerDate = registerDate
        self.lastConnectionDate = lastConnectionDate
        self.avatar = avatar
        self.site = site
        self.description = description
        self.firstName = firstName
        self.lastName = lastName
        self.token = token


