class CartPage:

    def __init__(self, page):
        self.page = page

    def checkout(self):
        self.page.click("#checkout")