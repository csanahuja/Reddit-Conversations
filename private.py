class Credentials:
    """ Class to read from file the credentials
    Format of the file:
        username <user>
        password <pass>
        client_id <id>
        client_secret <id>
        user_agent <user_agent>

    Check https://praw.readthedocs.io/en/latest/ to known how to get the values
    """

    def __init__(self, credentials):
        for line in open(credentials,'r'):
            line_args = line.split()

            if line_args[0] == "username":
                self.username = line_args[1]
            if line_args[0] == "password":
                self.password = line_args[1]
            if line_args[0] == "client_id":
                self.client_id = line_args[1]
            if line_args[0] == "client_secret":
                self.client_secret = line_args[1]
            if line_args[0] == "user_agent":
                self.user_agent = " ".join(line_args).split("user_agent ")[1]

    def username(self):
        return self.username
    def password(self):
        return self.password
    def client_id(self):
        return self.client_id
    def client_secret(self):
        return self.client_secret
    def user_agent(self):
        return self.user_agent
