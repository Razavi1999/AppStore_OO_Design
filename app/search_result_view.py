# from main import home_page

class SearchResultView:
    """docstring for SearchResultView."""

    def __init__(self):
        self.applications = []

    def display(self, **kwargs):
        print('---- SearchResultView -----')
        for each in self.applications:
            print(each.name)
        print('----- End SearchResultView -----')

    def search(self , categories, wanted):
        for category in categories:
            for app in category.applications:
                if(wanted == app.name):
                    self.applications.append(app)



    def appPressHandler(self, index , user):
        self.applications[index].update_views(user)
