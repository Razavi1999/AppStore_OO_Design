class  Application:
    """docstring for (Application)
    Application class with Attributes and Functions
    ."""

    def __init__(self , icon , images , trailer, description , type , price, size , developer):
        self.icon = icon
        self.images = images
        self.trailer = trailer
        self.description = description
        self.type = type
        self.price = price
        self.comments = []
        self.downloads_rate = 0
        self.user_views_rate = 0
        self.downloaded_users = []
        self.viewed_users = []
        self.size = size
        self.developer = developer

    def display(self, **kwargs):
        pass

    def insert_comment(self, **kwargs):
        pass

    def delete_comment(self, **kwargs):
        pass

    def install(self, **kwargs):
        pass

    def update_views(self, **kwargs):
        pass

    def update_downloads(self, **kwargs):
        pass
