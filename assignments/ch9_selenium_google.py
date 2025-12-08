from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
def google_search(query):
    driver = webdriver.Firefox()
    driver.get('https://www.google.com')
    elem = driver.find_element(By.NAME, 'q')
    elem.send_keys(query)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    title = driver.title
    driver.quit()
    return title
if __name__ == '__main__':
    print(google_search('Python Web Scraping'))
