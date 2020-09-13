import logging
from selenium import webdriver

logger = logging.getLogger(__name__)

class Scraping():
    data = None
    def __init__(self, chromedriver_path, google_chrome_bin):
        chrome_options = webdriver.ChromeOptions()

        if google_chrome_bin:
            chrome_options.binary_location = google_chrome_bin
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
            executable_path=chromedriver_path, chrome_options=chrome_options,
        )
        self.driver.implicitly_wait(30)

    def main(self):
        self.__scraping()
        self.__finish()
        return self.data

    def __scraping(self):
        # TODO implement this
        self.data = {}

    def __finish(self):
        self.driver.quit()