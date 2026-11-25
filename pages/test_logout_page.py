from playwright.sync_api import Page, expect
from reusables.test_reuable_methods import Reusable
from pages.test_loginpage import LoginPage

class Logout:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.rMeth = Reusable()
        self.login = LoginPage(page)
        self.logged_in_as = page.get_by_role("listitem").filter(has_text= "Logged in as")
        self.logout_btn = page.get_by_role("link", name= " Logout")
        self.login_to_acct_header = page.get_by_role("heading", name = "Login to your account")

    def test_logout(self):
        self.login.test_login("testani@test.com", "test@123")
        expect(self.logged_in_as).to_be_visible()
        self.rMeth.highlight_element(self.logged_in_as)
        expect(self.logout_btn).to_be_visible()
        self.rMeth.highlight_element(self.logout_btn)
        self.logout_btn.click()
        expect(self.login_to_acct_header).to_be_visible()
        self.rMeth.highlight_element(self.login_to_acct_header)
