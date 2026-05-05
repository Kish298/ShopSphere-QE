from pages import home_page


def test_post_visible_in_ui(page, create_post):

    post_id = create_post["id"]

    page.goto(f"https://jsonplaceholder.typicode.com/posts/{post_id}")

    text = home_page.get_post_text()

    assert "sunt aut facere" in text