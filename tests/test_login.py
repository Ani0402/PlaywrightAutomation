from playwright.sync_api import Page, expect
from pages.test_loginpage import LoginPage
import re, pytest

def load_from_csv() -> list:
    import csv
    data = []
    with open('./test-data/login_data.csv', newline = '') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data
@pytest.mark.parametrize(
    "emailaddress, password", load_from_csv()
)
def test_signup(page: Page, emailaddress, password):
    loginPage = LoginPage(page)

    page.goto("https://www.automationexercise.com/")
    expect(page).to_have_title(re.compile("Automation Exercise"))
    print("Page have title: Automation Exercise")
    # loginPage.test_login("testani@test.com", "test@123")
    loginPage.test_login(emailaddress, password)