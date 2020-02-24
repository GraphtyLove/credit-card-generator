"""File to scrap randomly generated credit cards."""
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

NUMBER_OF_CARD_TO_SCRAP = 2000

driver = webdriver.Firefox()
for i in range(NUMBER_OF_CARD_TO_SCRAP):
    driver.get('https://graphtylove.github.io/card-generator/')
    driver.save_screenshot("cards_data/screen-" + str(i) + ".png")