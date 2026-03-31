from .shopPage import ShopPage


class LoginPractisePage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    def login(self, username, password):
        self.page.get_by_role("textbox", name="Username:").fill(username)
        self.page.get_by_role("textbox", name="Password:").fill(password)
        self.page.get_by_role("checkbox", name="I Agree to the terms and conditions").check()
        self.page.get_by_role("button", name="Sign In").click()
        self.page.wait_for_url("**/angularpractice/shop")
        return ShopPage(self.page)
