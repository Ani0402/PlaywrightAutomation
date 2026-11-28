from playwright.sync_api import Page, expect
from reusables.test_reuable_methods import Reusable

class ProductPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.rMeth = Reusable()
        self.products_link = page.get_by_role("listitem").get_by_role("link", name = "Products")
        self.allproducts_heading = page.get_by_role("heading", name = "All Products")
        self.search_products_heading = page.get_by_role("heading", name = "Searched Products")
        self.search_box = page.locator("[id = 'search_product']")
        self.search_btn = page.locator("[id = 'submit_search']")
        self.products_list = page.locator(".features_items > .col-sm-4")

    def test_productsPage(self):
        expect(self.products_link).to_be_visible()
        self.rMeth.highlight_element(self.products_link)
        self.products_link.click()
        expect(self.allproducts_heading).to_be_visible()
        self.allproducts_heading.scroll_into_view_if_needed()
        self.rMeth.highlight_element(self.allproducts_heading)
        expect(self.search_box).to_be_visible()
        self.rMeth.highlight_element(self.search_box)
        self.search_box.fill("Top")
        self.search_btn.click()
        expect(self.search_products_heading).to_be_visible()
        self.rMeth.highlight_element(self.search_products_heading)
        self.search_products_heading.scroll_into_view_if_needed()
        expect(self.products_list.first).to_be_visible()
        self.products_list.first.scroll_into_view_if_needed()


        




