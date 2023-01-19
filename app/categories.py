class Categories:
    """docstring for Categories.
        each Application should be in one Category
    """

    def __init__(self , title):
        self.title = title
        self.applications = []

    def display(self, **kwargs):
        pass

    def add_app(self, **kwargs):
        pass

    def delete_app(self, **kwargs):
        pass
