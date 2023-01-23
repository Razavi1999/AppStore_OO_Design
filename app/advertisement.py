class Advertisement:
    """Advertisement in the HomePage of AppStore."""

    def __init__(self, title , image):
        self.title = title
        self.image = image

    def display(self):
        print('--- Advertisement info ---')

        print(f'title : {self.title} , image : {self.image}')

        print('--- info ended ---')
