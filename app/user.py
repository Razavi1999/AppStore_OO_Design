class User:
    """docstring for User."""

    def __init__(self , name , image , email):
        self.email = email
        self.name = name
        self.installed_apps = []
        self.image = image

    def download(self, application):
        self.installed_apps.append(application)
