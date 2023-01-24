class Developer:
    """docstring for Developer."""

    def __init__(self, name, icon):
        self.name = name
        self.icon = icon

    def update_application(self, app, name , icon , images , trailer, description , type , price):
        if app.developer == self:
            app.name = name
            app.icon = icon
            app.images = images
            app.trailer = trailer
            app.description = description
            app.type = type
            app.price = price
            return True
        return False
