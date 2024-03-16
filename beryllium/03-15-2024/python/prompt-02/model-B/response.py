import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Replace `URL` with the actual URL of the news website's homepage
URL = "https://www.eugenechevski.com/"

driver = selenium.webdriver.Chrome()
driver.get(URL)

# Wait for the page to load and JavaScript to complete
WebDriverWait(driver, 30).until(lambda d: d.execute_script('return document.readyState') == 'complete')

titles = driver.find_elements_by_css_selector("main")

# Print the extracted data
for title in titles:
    print(f"Title: {title.text}")

driver.quit()