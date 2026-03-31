from playwright.sync_api import expect


class ShopPage:

    def __init__(self, page):
        self.page = page

    def verifyProductPresent(self, productName):
        product = self.page.get_by_role("heading", name=productName, level=4)
        expect(product).to_be_visible()
