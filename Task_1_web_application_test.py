
#Prerequisites:
  #Install pytest using pip isntall pytest.
  #Install the Selenium WebDriver library using pip install selenium.
  #Download  ChromeDriver for Chrome  and ensure it's in your system's PATH.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Constants for login credentials
USERNAME = "admin"
PASSWORD = "admin"

# Initialize the WebDriver for chrome 
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Test case for logging in and verifying about_us page
def test_login_and_verify_button(browser):
    try:
        # Open the web page 
        browser.get("https://play1.automationcamp.ir/login.html")  

        # Log in with valid credentials
        username_field = browser.find_element(By.ID, "user")  
        password_field = browser.find_element(By.ID, "password")  
        login_button = browser.find_element(By.ID, "login") 

        username_field.send_keys(USERNAME)
        password_field.send_keys(PASSWORD)
        login_button.click()

        # Find the "Add to Cart" button and verify its presence
        add_to_cart_button = browser.find_element(By.ID, "submit_button")  

        # Assert that the button is displayed
        assert add_to_cart_button.is_displayed(), "Add to Cart button is not displayed on the page."


        
    except Exception as e:
        # Handle exceptions
        pytest.fail(f"Test failed with exception: {str(e)}")

if __name__ == "__main__":
    pytest.main(["-v", "Task_1_web_application_test.py"])
