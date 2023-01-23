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
        print('---------------- Application -------------------------')
        print('---------------- below is description of Application ------------------')
        for each in **kwargs:
            print(each)

    def insert_comment(self, **kwargs):
        comment = Comment()

        for k, v in kwargs.items():
            comment.k = v

        self.comments.append(comment)
        print('-------- new comment inserted ----------')


    def delete_comment(self, **kwargs):
        pass

    def install(self, **kwargs):
        pass

    def update_views(self, **kwargs):
        pass

    def update_downloads(self, **kwargs):
        pass
