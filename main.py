import logging
import time

from src.usecase import Usecase

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def main():
    logger.info("start scraping.")
    start = time.perf_counter()
    Usecase().run()
    end = time.perf_counter()
    logger.info(f"finish scraping ({(end - start):.2f} seconds took for scraping).")


if __name__ == "__main__":
    main()
