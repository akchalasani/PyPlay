
# pytest --browser_name chrome -m smoke -n 3 --tracing on --html=report.html
# pytest -k web_api     # search and only run tests with given matching name e.g. web_api
import json, pytest

from playwright.sync_api import Playwright, expect
from Utils.apiBaseFramework import APIUtils     #apiBase
from pageObjects.login import LoginPage
from pageObjects.dashBoard import DashboardPage

# Json file-> util-> access into test.
with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']
    
@pytest.mark.parametrize('user_credentials', user_credentials_list)     # 'user_credentials' is just a parameter here.

def test_e2e_web_api(playwright:Playwright, browserInstance, user_credentials):      # user_credentials is a FIXTURES here.
    
    userName = user_credentials["userEmail"]
    userPassword = user_credentials["userPassword"]

    # Create order -> order Id
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)
    
    # Login
    loginPage = LoginPage(browserInstance)     # object for loginPage class
    loginPage.navigate()
    dashboardPage = loginPage.login(userName, userPassword)
    
    # DashBoard Page
    OrdersHistoryPage = dashboardPage.selectOrdersNavLink()
    OrderDetailsPage = OrdersHistoryPage.selectOrder(orderId)
    OrderDetailsPage.verifyOrderMessage()

