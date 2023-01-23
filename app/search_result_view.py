class SearchResultView:
    """docstring for SearchResultView."""

    def __init__(self):
        self.applications = []

    def display(self):
        print('---- SearchResultView -----')
        for each in self.applications:
            each.display()
        print('----- End SearchResultView -----')

    def search(self , categories, wanted):
        for category in categories:
            for app in category.applications:
                if(wanted in app.name):
                    self.applications.append(app)
                    self.display()

        return self.applications


    def appPressHandler(self, index , user):
        self.applications[index].update_views(user)
