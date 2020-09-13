import dotenv
import logging
import os
import time

from src.service import ScraperService

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

dotenv.load_dotenv()
CHROMEDRIVER_PATH = os.environ.get("CHROMEDRIVER_PATH", "")
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "")
DATABASE_URL = os.environ.get("DATABASE_URL")


def main():
    logger.info("start scraping.")
    start = time.perf_counter()
    ScraperService(CHROMEDRIVER_PATH, GOOGLE_CHROME_BIN, DATABASE_URL).run()
    end = time.perf_counter()
    logger.info(f"finish scraping ({(end - start):.2f} seconds took for scraping).")


if __name__ == "__main__":
    main()
