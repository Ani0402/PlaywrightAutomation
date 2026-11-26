from playwright.sync_api import Page, expect
from pages.test_cart import CartPage
from collections import defaultdict
import re

class LoginPage:
    def __init__(self, page: Page):
        self.cartPage = CartPage(page)
        self.page = page
        self.signup_btn = page.get_by_role("link", name= " Signup / Login")
        self.logout_btn = page.get_by_role("link", name= " Logout")
        self.login_password = page.locator("[data-qa = 'login-password']")
        self.emailadd = page.locator("[data-qa = 'login-email']")
        self.loginbtn = page.get_by_role("button", name= " Login")
        self.product1_addToCart = page.get_by_role("button", name= "Add to cart")
        self.product_add_succ_msg = page.get_by_text("Your product has been added to cart.")
        self.continue_shop_btn = page.get_by_role("button", name = "Continue Shopping")
        self.product_name = page.locator(".product-information").get_by_role("heading", name = "Blue Top")
        self.productsList = []
        self.productDict = defaultdict(int)
        self.quantity = 0
        self.view_product_btn = page.locator("//a[@href = '/product_details/1']")
        self.home_btn = page.get_by_role("link", name = " Home")

    def product_add(self):
        self.view_product_btn.scroll_into_view_if_needed()
        self.view_product_btn.click()
        self.page.wait_for_timeout(2000)
        self.productsList.append(self.product_name.inner_text())
        self.product1_addToCart.scroll_into_view_if_needed()
        self.page.wait_for_timeout(2000)
        self.product1_addToCart.click()
        print("Successfully add to cart")
        expect(self.product_add_succ_msg).to_be_visible()
        self.continue_shop_btn.click()
        for item in self.productsList:
            self.productDict[item] += 1
        self.quantity = self.productDict[item]
        self.home_btn.click()

    def test_login(self, emailaddr, password):
        self.signup_btn.click()
        self.emailadd.fill(emailaddr)
        self.login_password.fill(password)
        self.loginbtn.click()
        expect(self.logout_btn).to_be_visible()

        self.page.wait_for_timeout(3000)
        self.product_add()
        # Cart functionality
        self.cartPage.test_cartCheck(self.quantity)

