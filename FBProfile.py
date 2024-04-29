import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException



# Specify the path to the ChromeDriver executable
chrome_driver_path = 'your_path'
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
# Create a Service object
service = Service(chrome_driver_path)

# Launch the Chrome web driver
driver = webdriver.Chrome(service=service,options=chrome_options)
driver.get('https://www.facebook.com')
driver.maximize_window()

# Replace 'email' and 'password' with your Facebook credentials
email = "your email"
password = "your Password"

# Find the email field and enter the email
email_field = driver.find_element(By.ID, 'email')
email_field.send_keys(email)

# Find the password field and enter the password
password_field = driver.find_element(By.ID, 'pass')
password_field.send_keys(password)




# Submit the login form
password_field.submit()

# Wait for the page to load (adjust the sleep time as needed)
time.sleep(5)

# Go to your Facebook profile
driver.get('https://www.facebook.com/me')

# Wait for the page to load (adjust the sleep time as needed)
time.sleep(5)


while True:
    # Scroll to the bottom of the page
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    
    # Wait for the page to load
    time.sleep(2)
    
    # Find all posts on the page
    posts = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]')
    

    
    # Process posts with "Friends" privacy
    for post in posts:
        privacy_img = '//img[@class="x1b0d499 x1d69dk1"]'
        privacy_elements = post.find_elements(By.XPATH, privacy_img)

        for privacy_element in privacy_elements:
            privacy_alt = privacy_element.get_attribute('alt')

            if privacy_alt == 'Only me':
                continue

            if privacy_alt == 'Friends':
                try:
                    # Scroll to the element's location
                    driver.execute_script("arguments[0].scrollIntoView();", privacy_element)

                    # Wait for the element to become visible
                    wait = WebDriverWait(driver, 20)
                    wait.until(EC.visibility_of(privacy_element))

                    # Check if the post is already set to "Only me"
                    if privacy_element.get_attribute('alt') != 'Only me':
                        # Click the privacy element using JavaScript
                        driver.execute_script("arguments[0].click();", privacy_element)

                        # Wait for the edit action to complete (if necessary)
                        time.sleep(3)

                        only_me_option = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[6]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[5]/div/div[1]/div[2]')
                        # Click the "Only me" option
                        only_me_option.click()

                        # Wait for the save button to become clickable
                        save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[6]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div')))

                        # Click the save button
                        save_button.click()

                        # Wait for the save action to complete (if necessary)
                        time.sleep(3)

                except Exception as e:
                    print(f"Exception: {str(e)}")
    
   


    # Close the driver
    driver.quit()
