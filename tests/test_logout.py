from playwright.sync_api import Page, expect
from pages.test_logout_page import Logout
import re

def test_logout(page: Page):
    logout = Logout(page)
    page.goto("https://www.automationexercise.com/")
    expect(page).to_have_title(re.compile("Automation Exercise"))
    logout.test_logout()
