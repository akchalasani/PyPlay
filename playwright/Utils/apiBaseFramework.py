from playwright.sync_api import Playwright
ordersPayLoad = {"orders":[{"country":"India","productOrderedId":"6960eac0c941646b7a8b3e68"}]}

class APIUtils:
    
    def getToken(self, playwright: Playwright, user_credentials):
        user_Email = user_credentials['userEmail']
        user_Password = user_credentials['userPassword']
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        
        response = api_request_context.post(
            "/api/ecom/auth/login", 
            data={"userEmail": user_Email,"userPassword": user_Password}
        )
        
        print(f"Status: {response.status}")
        print(f"Body: {response.text()}")
        assert response.ok, f"Login failed with status {response.status}: {response.text()}"
        return response.json()['token']
                                 
    def createOrder(self, playwright:Playwright, user_credentials):
        token = self.getToken(playwright, user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data = ordersPayLoad, 
                                 headers={"Authorization": token, 
                                 "Content-Type": "application/json"
                                 })
        print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId