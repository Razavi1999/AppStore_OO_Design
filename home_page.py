from SearchResultView import SearchResultView

class HomePage:
    def __init__(self , SearchResultView) -> None:
        self.advertisments = []
        self.search_box = SearchResultView()
        self.top_apps_view = []
        self.categories = []

    def display(self):
        pass

    def add_advertisment(self, **kwargs):
        pass

    def add_category(self, **kwargs):
        pass
