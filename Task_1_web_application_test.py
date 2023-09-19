
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
def test_login_and_verify_about_us(browser):
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

        # Navigate to the Contact_us page 
        about_us_link = browser.find_element(By.XPATH, "//a[contains(text(), 'Contact_Us')]")  
        about_us_link.click()

        # Verify the presence of contact details (email address and phone number)
        email_element = browser.find_element(By.XPATH, "//div[contains(text(), 'Email:')]")
        phone_element = browser.find_element(By.XPATH, "//div[contains(text(), 'Phone:')]")

        assert email_element.is_displayed()
        assert phone_element.is_displayed()

    except Exception as e:
        # Handle exceptions
        pytest.fail(f"Test failed with exception: {str(e)}")

if __name__ == "__main__":
    pytest.main(["-v", "Task_1_web_application_test.py"])
