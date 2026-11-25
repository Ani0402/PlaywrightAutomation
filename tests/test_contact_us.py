from playwright.sync_api import Page, expect
from pages.test_contactus_page import ContactUs
import re, pytest

def test_contact_us(page: Page):
    contactus = ContactUs(page)

    page.goto("https://www.automationexercise.com/")
    expect(page).to_have_title(re.compile("Automation Exercise"))
    print("Page have title: Automation Exercise")

    contactus.test_contactUs()