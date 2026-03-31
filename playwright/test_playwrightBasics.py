import time

from playwright.sync_api import Page, Playwright, expect

# global fixture -> PlayWright
def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()   # e.g. to test multi user login in fresh browser, without storing cookies and cache, e.g. incognito window. 
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")
    
# page: chromium headless mode, 1 single context
def test_playwrightShortCut(page:Page):             # pytest .\test_playwrightBasics.py::test_playwrightShortCut --headed
    page.goto("https://rahulshettyacademy.com")
    
#-- #terms(ID)  .text-info(CLASS NAME)  tagName(TAG NAME)
def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2X")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()      # css locator
    page.get_by_role("link", name = "terms and conditions").click()
    page.get_by_role("button", name = "Sign In").click()
    
    # Incorrect username/password - assertion
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    
def test_firefoxBrowser(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=True)
    page = firefoxBrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2X")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()      # css locator
    page.get_by_role("link", name = "terms and conditions").click()
    page.get_by_role("button", name = "Sign In").click()
    
    # Incorrect username/password - assertion
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)
    

        