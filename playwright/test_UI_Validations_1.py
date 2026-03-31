import time
from playwright.sync_api import Page, expect

def test_UI_ValidationDynamicScript(page:Page):
    #iphone x, Nokia Edge -> verify 2 items are showing in cart.
    
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()      # css locator
    page.get_by_role("link", name = "terms and conditions").click()
    page.get_by_role("button", name = "Sign In").click()
    
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)    
    expect(page.get_by_text("iphone X")).to_be_visible()
    expect(page.get_by_text("Nokia Edge")).to_be_visible()
    time.sleep(5)
    
    
def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    
    # python closure syntax: with
    with page.expect_popup() as newPage_info:
        page.get_by_role("link", name = "Free Access to InterviewQues", exact=False).click()       #new_page
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()
        print(text)                 # Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words = text.split("at")    # [0]-> Please email us at  #[1] mentor@rahulshettyacademy.com with below template to receive response
        email = words[1].strip().split(" ")[0] # [0] -> mentor@rahulshettyacademy.com      # [1] -> with below template to receive
        
        # pytest assertion
        assert email == "mentor@rahulshettyacademy.com"
        
        time.sleep(5)