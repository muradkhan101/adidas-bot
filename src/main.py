import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import helpers.links as Link

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1280x720")
chrome_options.add_argument("user-agent=Mozilla/5.0\ (Macintosh;\ Intel\ Mac\ OS\ X\ 10.12;\ rv:58.0)\ Gecko/20100101\ Firefox/58.0")

driver = webdriver.Chrome(executable_path=os.path.abspath("src/bin/chromedriver"), chrome_options=chrome_options)

url = Link.makeUrlWithSize('BB6170', 8)

driver.get(url)  # D97048

addToCart = driver.find_element(By.CSS_SELECTOR, "button.gl-cta.btn-bag.gl-cta--primary.gl-cta--full-width") 
addToCart.click()

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.gl-cta.gl-cta--secondary.gl-cta--full-width')))
checkoutButton = driver.find_element(By.CSS_SELECTOR, 'a.gl-cta.gl-cta--secondary.gl-cta--full-width')
checkoutButton.click()
print('MADE IT HERE!')