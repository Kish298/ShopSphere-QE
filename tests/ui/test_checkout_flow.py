from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout_flow(page):

    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    login.navigate()
    login.login("standard_user", "secret_sauce")

    inventory.add_first_product_to_cart()
    inventory.go_to_cart()

    cart.checkout()

    checkout.enter_details("Kishan", "QA", "400001")
    checkout.finish_order()

    confirmation = checkout.get_confirmation()

    assert "Thank you for your order!" in confirmation
    