class TopAppsView:
    """docstring for TopAppsView.
     TopAppsView section in HomePage
    """

    def __init__(self):
        self.applications = []

    def display(self, **kwargs):
        print('---- TopAppsView ---- ')

        for each in self.applications:
            print(each.name)

        print('---- End TopAppsView ----')

    def insert_application(self , categories):
        max = 0

        for category in categories:
            for app in category.applications:
                if app.downloads_rate > max:
                    self.applications.append(app)
                    max = app.downloads_rate
        self.display()

    def delete_application(self, application):
        self.applications.remove(application)
