import pytest

from pages.home_page import HomePage

@pytest.mark.ui
@pytest.mark.regression
def test_homepage_title(page):

    homepage = HomePage(page)

    homepage.navigate()

    assert "JSONPlaceholder" in homepage.get_title()