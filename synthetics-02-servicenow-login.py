# AppDynamics Synthetics Example 2 - Login to http://signon.service-now.com/ssologin.do/
#
# Maintainer David Ryder
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.chrome.options import Options
import codecs
import datetime, time, sys

# Initialize the synthetics browser driver
if "driver" not in dir(): # Run from command line
    print( "Driver provided by operating system environment")
    chromeDriverExe = "/usr/local/bin/chromedriver"
    options = Options()
    driver = webdriver.Chrome(executable_path=chromeDriverExe, options=options)
else:
    print( "Driver provided by AppDynamics Synthetics environment")

driver.implicitly_wait(15)
waitTimeout = 30
startTime = datetime.datetime.now()

# Configure the authentication information
userNameStr = "first.last@example.com"
userPasswordStr = "Required1"

# Navigate to the base url: "http://signon.service-now.com/ssologin.do/"
driver.get("http://signon.service-now.com/ssologin.do/")

# Wait for username text box to become visible, clear and then enter user name
id = WebDriverWait(driver, waitTimeout).until(EC.presence_of_element_located((By.ID, "username")))
id.clear()
id.send_keys(userNameStr)

# Wait for Next button to become visible and then click it
id = WebDriverWait(driver, waitTimeout).until(EC.presence_of_element_located((By.ID, "usernameSubmitButton")))
id.click()

# Wait for password text box to become visible, clear and then enter the password
id = WebDriverWait(driver, waitTimeout).until(EC.presence_of_element_located((By.ID, "password")))
id.clear()
id.send_keys(userPasswordStr)

# Wait for  Submit button to become visible and then click it
id = WebDriverWait(driver, waitTimeout).until(EC.presence_of_element_located((By.ID, "submitButton")))
id.click()

# Validate login occured
# Search for presense of "Welcome to Surf"
time.sleep(5)

# Capture a screenshot to the file postLogin.png
driver.save_screenshot("postLogin.png")
time.sleep( 5 )

# Logout
driver.get("https://signon.service-now.com/logout.do/")

# Report script is complete
print( "Complete {}".format(int((datetime.datetime.now() - startTime).total_seconds())))
# End Script
