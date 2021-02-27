import logging
import os
import time

import dotenv
from selenium import webdriver

logger = logging.getLogger(__name__)


dotenv.load_dotenv()
CHROMEDRIVER_PATH = os.environ.get("CHROMEDRIVER_PATH", "")
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "")

ROOT_URL = "" # TODO set root url

class Scraping():
    def __init__(self):
        self.data = []
        chrome_options = webdriver.ChromeOptions()

        if GOOGLE_CHROME_BIN:
            chrome_options.binary_location = GOOGLE_CHROME_BIN
            chrome_options.add_argument("--headless")

        chrome_options.add_argument("--disable-application-cache")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--enable-logging")
        chrome_options.add_argument("--hide-scrollbars")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--proxy-server="direct://"')
        chrome_options.add_argument("--proxy-bypass-list=*")
        chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(
            executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options,
        )
        self.driver.implicitly_wait(30)

    def main(self):
        self.__prepare()
        self.__scraping()
        self.__finish()
        return self.data

    def __prepare(self):
        self.driver.get(ROOT_URL)
        # TODO implement prepare logic

    def __scraping(self):
        # TODO implement scraping logic
        pass

    def __finish(self):
        self.driver.quit()