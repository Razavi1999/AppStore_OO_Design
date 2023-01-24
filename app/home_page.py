from search_result_view import SearchResultView
from categories import Categories
from advertisement import Advertisement
from top_apps_view import TopAppsView

class HomePage:
    def __init__(self):
        self.advertisements = []
        self.search_box = SearchResultView()
        self.top_apps_view = TopAppsView()
        self.categories = []

    def display(self, **kwargs):
        print('------ HomePage info --------')

        print('------ categories ------')
        for each in self.categories :
            print(each.title)

        print('------ top_apps_view ------')
        for each in self.top_apps_view.applications:
            print(each.name)

        print('------ advertisments ------')
        for each in self.advertisements:
            print(each.title)

        print('------ info ended ------')


    def add_advertisement(self, title , image):
        advertisement = Advertisement(title , image)
        self.advertisements.append(advertisement)
        print(f'*** New Advertisement {advertisement.title} added ***')
        return advertisement

    def add_category(self, title):
        category = Categories(title)
        self.categories.append(category)
        print(f'*** New Category {category.title} added ***')
        return category

    def search(self , name):
        return self.search_box.search(self.categories , name)

    def insert_app_to_topAppsView(self):
        self.top_apps_view.insert_application(self.categories)
