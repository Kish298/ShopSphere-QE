from pages.home_page import HomePage

def test_homepage_title(page):

    homepage = HomePage(page)

    homepage.navigate()

    assert "JSONPlaceholder" in homepage.get_title()