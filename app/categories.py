from application import Application

class Categories:
    """ docstring for Categories.
        each Application should be in one Category
    """

    def __init__(self , title):
        self.title = title
        self.applications = []

    def display(self, **kwargs):
        print('------ Category info --------')
        print('------ applications ------')
        for each in self.applications :
            print(each.name)
        print('------ info ended ------')

    def add_app(self, name , icon , images , trailer, description , type , price, size , developer):
        application = Application(
            name , icon , images ,
            trailer, description , type ,
            price, size , developer
        )
        self.applications.append(application)
        return application

    def delete_app(self, application):
        self.applications.remove(application)
