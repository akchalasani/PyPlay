import pytest
from pageObjects.loginPractisePage import LoginPractisePage


# NOTE: The site updated the password. "learning" no longer works.
# Current valid password as shown by the site itself: "Learning@830$3mK2"
# Update USERNAME / PASSWORD below if credentials change again.
USERNAME = "rahulshettyacademy"
PASSWORD = "Learning@830$3mK2"


def test_loginAndVerifyIphoneXOnShopPage(browserInstance):
    loginPractisePage = LoginPractisePage(browserInstance)
    loginPractisePage.navigate()

    shopPage = loginPractisePage.login(USERNAME, PASSWORD)

    shopPage.verifyProductPresent("iphone X")
