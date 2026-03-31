from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# --- CONFIG ---
URL = "https://example.com/login"   # replace with actual URL
INVALID_USERNAME = "wrong_user"
INVALID_PASSWORD = "wrong_pass"
EXPECTED_ERROR = "Invalid username or password"  # update as per app

# --- SETUP ---
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    # 1. Open login page
    driver.get(URL)

    # 2. Enter incorrect username
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    username.send_keys(INVALID_USERNAME)

    # 3. Enter incorrect password
    password = driver.find_element(By.ID, "password")
    password.send_keys(INVALID_PASSWORD)

    # 4. Select "Employee" from dropdown
    dropdown = Select(driver.find_element(By.ID, "role"))  # update locator if needed
    dropdown.select_by_visible_text("Employee")

    # 5. Click Login button
    login_button = driver.find_element(By.ID, "loginBtn")
    login_button.click()

    # 6. Assert error message
    error_element = wait.until(
        EC.visibility_of_element_located((By.ID, "errorMessage"))  # update locator
    )
    actual_error = error_element.text

    assert EXPECTED_ERROR in actual_error, f"Expected '{EXPECTED_ERROR}', got '{actual_error}'"

    print("Test Passed: Error message validated successfully!")

finally:
    driver.quit()