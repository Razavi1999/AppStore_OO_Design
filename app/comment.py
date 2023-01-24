class Comment:
    """docstring for Comment.
        each user can insert Comment
        and that user can delete his or her Comment
    """

    def __init__(self , user, description , date):
        self.description = description
        self.date = date
        self.user = user
