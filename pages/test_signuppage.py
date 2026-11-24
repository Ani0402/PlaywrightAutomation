from playwright.sync_api import Page, expect
from reusables.test_reuable_methods import Reusable
import re

class SignUpPage:
    def __init__(self, page: Page):
        self.page = page
        self.emailaddr_alrdy_exits_msg = page.get_by_text("Email Address already exist!")
        self.signup_btn = page.get_by_role("link", name= " Signup / Login")
        self.namefield = page.locator("//input[@placeholder = 'Name']")
        self.emailadd = page.locator("[data-qa = 'signup-email']")
        self.submit_btn = page.get_by_role("button", name = 'Signup')
        self.pageTitle = page.get_by_text("Enter Account Information")
        self.male_btn = page.get_by_label("Mr.")
        self.female_btn = page.get_by_label("Mrs.")
        self.password = page.get_by_label("Password")
        self.daysDD = page.locator("[data-qa = 'days']")
        self.monthDD = page.locator("[data-qa = 'months']")
        self.yearDD = page.locator("[data-qa = 'years']")
        self.firstName = page.get_by_label("First name ")
        self.lastName = page.get_by_label("Last name ")
        self.address = page.locator("[id = 'address1']")
        self.countryDD = page.locator("[data-qa = 'country']")
        self.state = page.get_by_label("State ")
        self.city = page.get_by_label("City ")
        self.zipcode = page.get_by_label("Zipcode ")
        self.mobileNum = page.get_by_label("Mobile Number ")
        self.createAcctBtn = page.get_by_role("button", name = 'Create Account')

    def test_signup(self, username, emailaddr, gender, day, month, year, firstName, lastName, address, state, city, zipcode, mobile_num):
        rMeth = Reusable()
        self.signup_btn.click()
        self.namefield.fill(username)
        self.emailadd.fill(emailaddr)
        self.submit_btn.click()
        self.page.wait_for_timeout(2000)
        expect(self.pageTitle.or_(self.emailaddr_alrdy_exits_msg)).to_be_visible()
        if self.emailaddr_alrdy_exits_msg.is_visible():
            print("Email Address already exists")
            rMeth.highlight_element(self.emailaddr_alrdy_exits_msg)
        else:
            expect(self.pageTitle).to_have_text("Enter Account Information")
        print("Successfull signup page load up")
        if gender == "male":
            self.male_btn.click()
        else:
            self.female_btn.click()

        self.password.fill("test@123")
        self.daysDD.select_option(day)
        self.monthDD.select_option(month)
        self.yearDD.select_option(year)

        self.firstName.fill(firstName)
        self.lastName.fill(lastName)
        self.address.fill(address)
        self.countryDD.select_option("India")
        self.state.fill(state)
        self.city.fill(city)
        self.zipcode.fill(zipcode)
        self.mobileNum.fill(mobile_num)

        print("All details successfully entered")
        self.createAcctBtn.click()



        


        


            

            
        