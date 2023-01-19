from SearchResultView import SearchResultView

class HomePage:
    def __init__(self) -> None:
        self.advertisements = []
        self.search_box = SearchResultView(applications=[])
        self.top_apps_view = []
        self.categories = []

    def display(self):
        pass

    def add_advertisement(self, **kwargs):
        pass

    def add_category(self, **kwargs):
        pass
