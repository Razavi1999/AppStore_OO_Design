class Comment(object):
    """docstring for Comment.
        each user can insert Comment
        and that user can delete his or her Comment
    """

    def __init__(self, name , description , date):
        super(Comment, self).__init__()
        self.name = name
        self.description = description
        self.date = date
