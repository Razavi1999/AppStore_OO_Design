class User(object):
    """docstring for User."""

    def __init__(self, installedApps , name ,
        image , email):
        super(User, self).__init__()
        self.email = email
        self.name = name
        self.installedApps = installedApps
        self.image = image

    def download(self , application):
        pass
