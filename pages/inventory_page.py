class InventoryPage:

    def __init__(self, page):
        self.page = page

    def add_first_product_to_cart(self):
        self.page.click(".inventory_item button")

    def go_to_cart(self):
        self.page.click(".shopping_cart_link")