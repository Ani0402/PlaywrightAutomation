from playwright.sync_api import Page, expect
from pages.test_productsPage import ProductPage
import re

def test_products_page(page: Page):
    productPage = ProductPage(page)

    page.goto("https://www.automationexercise.com/")
    expect(page).to_have_title(re.compile("Automation Exercise"))
    print("Page have title: Automation Exercise")
    productPage.test_productsPage()