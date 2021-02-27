from enum import Enum

class ReservationStatus(Enum):
    INVALID = ("RESERVATION_STATUS_INVALID", "")
    # TODO add enum values

    def __init__(self, k, v):
        self.k = k
        self.v = v

    @classmethod
    def to_enum_value(cls, v):
        for c in [*cls.__members__.values()]:
            if v == c.v:
                return c.k
        return cls.INVALID.k


class ReservationDivision(Enum):
    INVALID = ("RESERVATION_DIVISION_INVALID", "")
    # TODO add enum values

    def __init__(self, k, v):
        self.k = k
        self.v = v

    @classmethod
    def to_enum_value(cls, v):
        for c in [*cls.__members__.values()]:
            if v == c.v:
                return c.k
        return cls.INVALID.k


class DayOfWeek(Enum):
    INVALID = ("DAY_OF_WEEK_INVALID", "")
    SUNDAY = ("DAY_OF_WEEK_SUNDAY", "日")
    MONDAY = ("DAY_OF_WEEK_MONDAY", "月")
    TUESDAY = ("DAY_OF_WEEK_TUESDAY", "火")
    WEDNESDAY = ("DAY_OF_WEEK_WEDNESDAY", "水")
    THUESDAY = ("DAY_OF_WEEK_THUESDAY", "木")
    FRIDAY = ("DAY_OF_WEEK_FRIDAY", "金")
    SATURDAY = ("DAY_OF_WEEK_SATURDAY", "土")

    def __init__(self, k, v):
        self.k = k
        self.v = v

    @classmethod
    def to_enum_value(cls, v):
        for c in [*cls.__members__.values()]:
            if v == c.v:
                return c.k
        return cls.INVALID.k
