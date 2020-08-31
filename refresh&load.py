from selenium import webdriver
import time
import pyautogui as pg
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--kiosk")
browser = webdriver.Chrome('C:\\work\\Selenium\\chromedriver.exe', chrome_options=chrome_options)
browser.get('https://app.powerbi.com/view?r=eyJrIjoiZTJhZTNhN2UtMGEzNi00ZDBmLWI5NzQtNjEzM2FjOGM5NjcxIiwidCI6IjBkMDUzNmNkLTJhYmQtNDExYi1hNDZlLWI0MzYwNzVlZmVhZiIsImMiOjh9')
while True:
    time.sleep(12)
    browser.switch_to.frame(browser.find_element_by_name("visual-sandbox"))
    pg.click(278,88)
    time.sleep(3)
    day = browser.find_element_by_class_name('cellsArea')
    days = []
    for ele in day.find_elements_by_css_selector("rect"):
        days.append(ele)
    days[-1].click()
    pg.click(1804,189)
    time.sleep(3600)
    browser.refresh()
    continue