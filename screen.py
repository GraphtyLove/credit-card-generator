from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Firefox()
for i in range(1000):
    driver.get('https://graphtylove.github.io/card-generator/')
    driver.save_screenshot("cards_data/screen-" + str(i) + ".png")