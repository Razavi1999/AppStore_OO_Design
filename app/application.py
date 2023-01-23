from comment import Comment

class  Application:
    """docstring for (Application)
    Application class with Attributes and Functions
    ."""

    def __init__(self , name , icon , images , trailer, description , type , price, size , developer):
        self.icon = icon
        self.name = name
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

    def display(self):
        print('---------------- Application -------------------------')
        print('---------------- below is description of Application ------------------')
        print(f' icon : {self.icon} , description : {self.description} , type : {self.type} , price : {self.price} , developer : {self.developer} , size : {self.size} ,')

        print('---- Comments ----')
        for each in self.comments:
            print(each.description)

    def insert_comment(self, user , name , description , date):
        comment = Comment(name , description , date)
        self.comments.append(comment)
        print('-------- new comment inserted ----------')
        print()
        print()
        self.display()
        return comment

    def delete_comment(self, comment):
        self.comments.remove(comment)

    def install(self, user):
        self.downloaded_users.append(user)
        print(f'{user.name} installed {self.name}')

    def update_views(self, user):
        self.user_views_rate = self.user_views_rate + 1
        self.viewed_users.append(user)

    def update_downloads(self, user):
        self.downloads_rate = self.downloads_rate + 1
        self.downloaded_users.append(user)
