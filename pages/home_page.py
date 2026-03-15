class HomePage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://jsonplaceholder.typicode.com")

    def get_title(self):
        return self.page.title()