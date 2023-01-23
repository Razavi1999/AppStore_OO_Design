class User:
    """docstring for User."""

    def __init__(self , name , image , email):
        self.email = email
        self.name = name
        self.installedApps = []
        self.image = image

    def download(self, **kwargs):
        pass
