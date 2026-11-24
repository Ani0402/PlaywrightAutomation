from playwright.sync_api import Page, expect
import re

class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.cart_btn = page.get_by_role("link", name = "Cart", exact = True)
        self.cart_rows = page.locator("//tr[contains(@id, 'product-')]")
        self.product_name = page.locator("//td[@class = 'cart_description']//a[text() = 'Blue Top']")
        self.product_count = page.locator("//td[@class = 'cart_quantity']/button")
        self.product_price = page.locator("//td[@class = 'cart_price']/p")
        self.product_total_price = page.locator("//td[@class = 'cart_total']/p")

    def test_cartCheck(self, quantity):
        self.cart_btn.click()
        expect(self.cart_rows).to_have_count(1)
        print("Cart is successfully working")
        expect(self.product_name).to_be_visible()
        print("Added product is visible")
        expect(self.product_count).to_have_count(1)
        price = float(re.sub(r"\D", "",self.product_total_price.inner_text()))
        expect(self.product_count).to_have_count(quantity)
        if price ==  int(self.product_count.inner_text()) * float(re.sub(r"\D", "",self.product_price.inner_text())):
            print("Total Price is functionality is working as per requirements")
        else:
            print("not working fine")
        



        