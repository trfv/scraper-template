import logging

from src.scraping import Scraping
from src.repository import Repository


logger = logging.getLogger(__name__)

class ScraperService():
    def __init__(self, chromedriver_path, google_chrome_bin, database_url):
        self.chromedriver_path = chromedriver_path
        self.google_chrome_bin = google_chrome_bin
        self.database_url = database_url

    def run(self):
        self.__scraping()
        self.__save()

    def __scraping(self):
        self.data = Scraping(self.chromedriver_path, self.google_chrome_bin).main()

    def __save(self):
        Repository(self.database_url).save(self.data)
