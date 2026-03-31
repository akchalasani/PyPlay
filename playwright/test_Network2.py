import time

from playwright.sync_api import Page, Playwright, expect

from Utils.apiBase import APIUtils

# before contacting the server:
# -> api call from the browser -> api call contact server return back response to browser -> browser use response to generate html

def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69c1ce4ff86ba51a6520da6c")
    
def test_network_2(page: Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",interceptRequest)
    page.get_by_placeholder("email@example.com").fill("akchalasani@hotmil.com")     
    page.get_by_placeholder("enter your passsword").fill("Anil1234!")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)
    
    
def test_session_storage(playwright:Playwright):
    api_utils = APIUtils()
    getToken = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # script to inject token in session local storage
    # javascript injection into browser: localstorage -> key value.
    page.add_init_script(f"""localStorage.setItem('token', '{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client/")  
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()  