class HomePage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://jsonplaceholder.typicode.com")
        self.page.wait_for_load_state("networkidle")

    def get_title(self):
        return self.page.title()
    
    def get_page_text(self):
        return self.page.content()
    
    def get_post_text(self):
        self.page.wait_for_selector("pre")
        return self.page.locator("pre").inner_text()