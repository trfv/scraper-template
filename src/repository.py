import logging

logger = logging.getLogger(__name__)

class Repository():
    def __init__(self, database_url):
        self.database_url = database_url

    def save(self, data):
        self.__insert(data)

    def __insert(self, data):
        # TODO implement this
        pass