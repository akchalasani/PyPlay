import time
from playwright.sync_api import Page, expect

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