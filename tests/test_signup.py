from playwright.sync_api import Page, expect
from pages.test_signuppage import SignUpPage
import re, pytest

def load_from_csv() -> list:
    import csv
    data = []
    with open('./test-data/signup_data.csv', newline = '') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data
@pytest.mark.parametrize(
    "name, emailaddr, gender, day, month, year, firstName, lastName, address1, state, city, zipcode, mobilenum", load_from_csv()
)
def test_signup(page, name, emailaddr, gender, day, month, year, firstName, lastName, address1, state, city, zipcode, mobilenum):
    signupPage = SignUpPage(page)

    page.goto("https://www.automationexercise.com/")
    expect(page).to_have_title(re.compile("Automation Exercise"))
    print("Page have title: Automation Exercise")
    # signupPage.test_signup("Admin123", "testani@test.com", "male", "5", "February", "1998", "ajsdad", "dwqwsd", "xyz street 123 Dillion Road", "Tamil Nadu", "Chennai", "600045", "1281821212")
    signupPage.test_signup(name, emailaddr, gender, day, month, year, firstName, lastName, address1, state, city, zipcode, mobilenum)
    





