import logging

from src.scraping import Scraping
from src.repository import Repository


logger = logging.getLogger(__name__)

class Usecase():
    def run(self):
        self.__scraping()
        self.__save()

    def __scraping(self):
        self.data = Scraping().main()

    def __save(self):
        Repository().save(self.data)
