class CheckoutPage:

    def __init__(self, page):
        self.page = page

    def enter_details(self, first, last, zip_code):
        self.page.fill("#first-name", first)
        self.page.fill("#last-name", last)
        self.page.fill("#postal-code", zip_code)
        self.page.click("#continue")

    def finish_order(self):
        self.page.click("#finish")

    def get_confirmation(self):
        return self.page.locator(".complete-header").inner_text()