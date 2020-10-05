# AppDynamics Synthetics Example 1 - Search Google
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
    print( "Driver provided by AppDynamics syntehtics environment")

driver.implicitly_wait(15)
waitTimeout = 30
startTime = datetime.datetime.now()

# Use Synthetics Credential Vault
searchStr = "<%GOOGLE_SEARCH_STR_1%>"
if searchStr.startswith("<"):
    print( "Credential Vault Key: {} missing".format(searchStr) )
    searchStr = "AppDynamics"
print( "Credential Vault Search Str: {}".format(searchStr))

# Navigate to the base url: https://www.google.com
driver.get("https://www.google.com")

# Wait for and validate the Google Search text box is present
id = WebDriverWait(driver, waitTimeout).until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))

# Clear the search box, Enter search text and press enter
id.clear()
id.send_keys(searchStr)
id.send_keys( Keys.ENTER )

# Wait for and validate the results stats are visible
id = WebDriverWait(driver, waitTimeout).until(EC.presence_of_element_located((By.ID, "result-stats")))
print( "Results stats {}".format(id.text) )

# Capture a screenshot to the file searchResults.png
driver.save_screenshot("searchResults.png")
time.sleep( 2 )

# Report script is complete
print( "Complete {}".format(int((datetime.datetime.now() - startTime).total_seconds())))
# End Script
