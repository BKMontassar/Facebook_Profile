# Facebook_Profile
Facebook Post Privacy Automation
Introduction
This project automates the process of changing all post privacy settings from public to "Only me" on Facebook profiles using Python and Selenium. It's designed to simplify privacy management for users who want to reset their Facebook accounts without Facebook's native reset option.

Prerequisites
Python 3.x
Selenium
ChromeDriver (download and specify the path in the code)
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/facebook-privacy-automation.git
Install Python dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
Replace 'email' and 'password' in config.py with your Facebook credentials.
Run the script:
bash
Copy code
python automate_privacy.py
How it Works
Launches a Chrome WebDriver using Selenium.
Logs into Facebook using provided credentials.
Navigates to the user's profile.
Scrolls down to load all posts.
Identifies posts with "Friends" privacy and changes them to "Only me".
Saves the changes for each post.
Customization
Adjust sleep times (time.sleep) for waiting periods as needed.
Modify XPaths and element locators to match changes in Facebook's UI.
Enhance exception handling to manage potential errors during execution.
Limitations
Relies on web scraping techniques, which may be affected by changes in Facebook's website structure.
May require periodic updates to maintain functionality.
