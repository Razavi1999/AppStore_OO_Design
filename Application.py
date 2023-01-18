class  Application(object):
    """docstring for (Application)
    Application class with Attributes and Functions
    ."""

    def __init__(self , icon , images , trailer ,
                description , type , price , comments ,
                downloaded_users , viewed_users ,
                 downloads_rate , user_views_rate ,
                 size , developer
                 ):
        self.icon = icon
        self.images = images
        self.trailer = trailer
        self.description = description
        self.type = type
        self.price = price
        self.comments = []
        self.downloads_rate = downloads_rate
        self.user_views_rate = user_views_rate
        self.downloaded_users = []
        self.viewed_users = []
        self.size = size
        self.developer = developer

    def display():
        pass

    def insert_comment(user):
        pass

    def delete_comment(user):
        pass

    def install():
        pass

    def update_views():
        pass

    def update_downloads():
        pass
