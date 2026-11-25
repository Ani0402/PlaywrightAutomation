from playwright.sync_api import Page, expect
from reusables.test_reuable_methods import Reusable

class ContactUs:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.rMeth = Reusable()
        self.contact_us_btn = page.get_by_role("listitem").filter(has_text= "Contact us")
        self.name = page.get_by_placeholder("Name")
        self.emailaddr = page.locator("[data-qa = 'email']")
        self.subject = page.get_by_placeholder("Subject")
        self.your_msg = page.get_by_placeholder("Your Message Here")
        self.fileUploadInput = page.locator("[name = 'upload_file']")
        self.submitBtn = page.locator("[data-qa = 'submit-button']")
        self.successMsg = page.locator(".status.alert.alert-success")

    def test_contactUs(self):
        expect(self.contact_us_btn).to_be_visible()
        self.rMeth.highlight_element(self.contact_us_btn)
        self.contact_us_btn.click()
        expect(self.name).to_be_visible()
        self.name.fill("testuser")
        expect(self.emailaddr).to_be_visible()
        self.emailaddr.fill("testani@test.com")
        self.subject.fill("Test Subject")
        self.your_msg.fill("This is Test Message")
        expect(self.fileUploadInput).to_be_visible()
        self.fileUploadInput.set_input_files("C:/Users/cubic/OneDrive/Documents/Appreciation Letter.docx")
        self.submitBtn.scroll_into_view_if_needed()
        self.page.on('dialog', lambda dialog: dialog.accept());
        self.submitBtn.click() 
        expect(self.successMsg).to_be_visible()
