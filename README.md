<!-- Facebook Post Privacy Automation -->
<h1 align="center">Facebook Post Privacy Automation</h1>

<!-- Introduction -->
<p align="center">This project automates the process of changing all post privacy settings from public to "Only me" on Facebook profiles using Python and Selenium. It's designed to simplify privacy management for users who want to reset their Facebook accounts without Facebook's native reset option.</p>

<!-- Prerequisites -->
<h2 align="center">Prerequisites</h2>
<p align="center">- Python 3.x</p>
<p align="center">- Selenium</p>
<p align="center">- ChromeDriver (download and specify the path in the code)</p>

<!-- Installation -->
<h2 align="center">Installation</h2>

The common commands for installing and using this project are:

* `git clone https://github.com/BKMontassar/facebook-privacy-automation.git` — Clones the repository to your local machine.
* `pip install -r requirements.txt` — Installs the Python dependencies required for this project.

<!-- Usage -->
<h2 align="center">Usage</h2>
<p align="center">1. Replace 'email' and 'password' in config.py with your Facebook credentials.</p>
<p align="center">2. Run the script:</p>
<p align="center">```bash</br>python automate_privacy.py```</p>

<!-- How it Works -->
<h2 align="center">How it Works</h2>
<p align="center">1. Launches a Chrome WebDriver using Selenium.</p>
<p align="center">2. Logs into Facebook using provided credentials.</p>
<p align="center">3. Navigates to the user's profile.</p>
<p align="center">4. Scrolls down to load all posts.</p>
<p align="center">5. Identifies posts with "Friends" privacy and changes them to "Only me".</p>
<p align="center">6. Saves the changes for each post.</p>

<!-- Customization -->
<h2 align="center">Customization</h2>
<p align="center">- Adjust sleep times (`time.sleep`) for waiting periods as needed.</p>
<p align="center">- Modify XPaths and element locators to match changes in Facebook's UI.</p>
<p align="center">- Enhance exception handling to manage potential errors during execution.</p>

<!-- Limitations -->
<h2 align="center">Limitations</h2>
<p align="center">- Relies on web scraping techniques, which may be affected by changes in Facebook's website structure.</p>
<p align="center">- May require periodic updates to maintain functionality.</p>

<!-- Contact Information -->
<h2 align="center">Contact Information</h2>
<p align="center">
  <a target="_blank" href="mailto:montassar.benkraiem@esprit.tn" style="margin-right: 10px;">
    <img alt="Gmail"  src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  
  <a target="_blank" href="https://www.linkedin.com/in/montassar-ben-kraiem-4a9a9713b/" style="margin-left: 10px;">
    <img alt="LinkedIn"  src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
</p>
