import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import helpers.manage_tabs as Tabs
from helpers.wait import wait_for_load

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1280x720")
chrome_options.add_argument("user-agent=Mozilla/5.0\ (Macintosh;\ Intel\ Mac\ OS\ X\ 10.12;\ rv:58.0)\ Gecko/20100101\ Firefox/58.0")

driver = webdriver.Chrome(executable_path=os.path.abspath("src/bin/chromedriver"), chrome_options=chrome_options)

driver.get("https://www.youtube.com/results?search_query=podcast") #Page

videos = driver.find_elements(By.TAG_NAME, "ytd-video-renderer") #FieldGroup

if len(videos) != 0:
    # for video_obj in videos:
    video_link = videos[1].find_element(By.ID, "video-title")
    print(driver.current_url)
    current_tab, new_tab = Tabs.open_tab(driver, video_link)
    wait_for_load(driver, By.ID, 'container')
    print(driver.current_url)
    #     continue

    title = driver.find_element(By.CLASS_NAME, "title").text #Field

    views = driver.find_element(By.CLASS_NAME, "view-count").text  #Field
    views = views[:views.index(" view")]

    date = driver.find_element(By.CLASS_NAME, "date").text #Field
    date = title[date.index(" on ") + 4:]

    likes = driver.find_element(By.XPATH, "//yt-formatted-string[contains(@aria-label, ' likes')]").getAttribute('aria-label') #Field
    likes = likes[:likes.index(' likes')]

    dislikes = driver.find_element(By.XPATH, "//yt-formatted-string[contains(@aria-label, ' dislikes')]").getAttribute('aria-label') #Field
    dislikes = dislikes[:dislikes.index(' dislikes')]

    print(title, views, date, likes, dislikes)
    Tabs.close_tab(driver, current_tab)
    print(driver.current_url)
else:
    print("nothing found")
