from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Safari driver
driver = webdriver.Safari()

# URL to scrape
url = "https://www.quikr.com/cars/used+cars+mumbai+w1079"
driver.get(url)

# Scroll logic for better data loading
def scroll_and_wait(scroll_times=5, short_wait=1, long_wait=8):
    """Scroll rapidly, then pause longer to ensure content loads."""
    last_height = driver.execute_script('return document.body.scrollHeight')

    while True:
        for _ in range(scroll_times):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(short_wait)  # Quick scroll

        time.sleep(long_wait)  # Longer wait for content to load

        new_height = driver.execute_script('return document.body.scrollHeight')
        
        if new_height == last_height:  # Stop if no new content appears
            break
        
        last_height = new_height

# Run improved scroll function
scroll_and_wait()

# Extract page source for BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

driver.quit()

# Save page content
with open("page_content_mumbai.html", "w", encoding="utf-8") as file:
    file.write(str(soup))
