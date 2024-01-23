from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--enable-javascript")  # Enable JavaScript

# Initialize Chrome browser with ChromeDriverManager
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
browser.implicitly_wait(5)  # Implicit wait for 5 seconds

# URL to open
url_to_open = "https://erpv4.deepsense.co.in/"  # Replace this with the desired URL

try:
    # Open the URL in the browser
    browser.get(url_to_open)

    # Find the email input element and enter the email
    email_input = browser.find_element(By.ID, 'login_email')
    email_input.send_keys("administrator")

    # Find the password input element and enter the password
    password_input = browser.find_element(By.ID, "login_password")
    password_input.send_keys("Deeperp14")

    # Submit the form by pressing Enter (assuming pressing Enter submits the form)
    password_input.send_keys(Keys.RETURN)

    # Wait for a few seconds (optional)
    time.sleep(2)

    browser.get("https://erpv4.deepsense.co.in/app/customer")

    # # Find the search input and enter "Customer List"
    # search_input = browser.find_element(By.ID, "navbar-search")
    # search_input.send_keys("Customer List")
    # search_input.send_keys(Keys.ENTER)

    # Wait for the page to load (adjust the sleep duration based on your page loading time)
    time.sleep(4)  # Wait for 5 seconds

    # # Find the input with value "500" and click it
    enter_button = browser.find_element(By.CSS_SELECTOR, 'button[data-value="500"]')
    enter_button.click()

    # Wait for the page to load again
    time.sleep(5)  # Wait for 5 seconds

    # Find all <a> tags with class name "ellipsis" and get their href attributes
    urls = [a.get_attribute("href") for a in browser.find_elements(By.CSS_SELECTOR, 'a.ellipsis') ]
    valid_urls = [url for url in urls if url is not None]
    print(valid_urls)
    print(len(urls))
    print(len(valid_urls))

    # Counter for custom_auto_field
    input_no = 1

    # Iterate through the URLs and perform actions
    for url in valid_urls:
        browser.get(url)
        time.sleep(2)  # Wait for 2 seconds
        
        # Click "More Information" div
        # more_info_div = browser.find_element(By.CSS_SELECTOR, 'div[data-fieldname="column_break2"]')  # for supplier table
        more_info_div = browser.find_element(By.CSS_SELECTOR, 'div[data-fieldname="more_info"]') # for customer table
        more_info_div.click()

        # Find the input with data-fieldname "custom_auto_field" and enter custom value
        custom_auto_field_input = browser.find_element(By.CSS_SELECTOR, 'input[data-fieldname="custom_auto_field"]')
        custom_auto_field_input.clear()
        time.sleep(2)  # Wait for 2 seconds

        
        # Set the pattern to CS-0001 for the first iteration, and then follow the specified pattern
        next_customer_id = "CS-0001" if input_no == 1 else f"CS-{input_no:04d}"

        custom_auto_field_input.send_keys(next_customer_id)


        # Find the button with data-label "Save" and click it
        # save_button = browser.find_element(By.CSS_SELECTOR, 'button[data-label="Save"]')
        # save_button.click()
        time.sleep(5)  # Wait for 2 seconds
        
        # Increment input_no for the next iteration
        input_no += 1

finally:
    # Close the browser window
    browser.quit()
