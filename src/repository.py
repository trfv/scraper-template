import io
import logging
import os
import time

import dotenv
import psycopg2

logger = logging.getLogger(__name__)

dotenv.load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL")

COLUMN_BUILDING = "building"
COLUMN_INSTITUTION = "institution"
COLUMN_DATE = "date"
COLUMN_DAY_OF_WEEK = "day_of_week"
COLUMN_RESERVATION = "reservation"
COLUMN_INSTITUTION_ID = "institution_id"
COLUMN_TOKYO_WARD = "tokyo_ward"

COLUMNS = [
    COLUMN_INSTITUTION_ID,
    COLUMN_TOKYO_WARD,
    COLUMN_BUILDING,
    COLUMN_INSTITUTION,
    COLUMN_DATE,
    COLUMN_DAY_OF_WEEK,
    COLUMN_RESERVATION,
]

TARGET_TOKYO_WARD = "TOKYO_WARD_XXXX" # TODO set target 

class Repository():
    def __init__(self):
        self.data = []

    def save(self, raw_data):
        self.__convert(raw_data)
        self.__update()

    def __to_dict_rows(self, d):
        # institution_id, building, institution, rows = d
        res = []
        # TODO implement convert logic
        return res

    def __convert(self, raw_data):
        for d in raw_data:
            new_data = self.__to_dict_rows(d)
            self.data.extend(new_data)

    def __update(self):
        f = io.StringIO()
        f.write(
            "\n".join("\t".join(str(d.get(col)) for col in COLUMNS) for d in self.data)
        )
        f.seek(0)

        logger.debug("copy data to database")
        start = time.time()
        with psycopg2.connect(DATABASE_URL, sslmode="require") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    f"delete from reservation where tokyo_ward = '{TARGET_TOKYO_WARD}';"
                )
                cur.copy_from(f, "reservation", sep="\t", columns=COLUMNS, null="None")

        end = time.time()
        logger.debug(f"{(end - start):.2f} seconds took for copying.")