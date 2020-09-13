import enum

class ReservationStatus(enum.Enum):
    INVALID = "RESERVATION_STATUS_INVALID"
    # TODO add enum values

    def to_enum(self, src):
        # TODO implement this method
        return self.INVALID


class ReservationDivision(enum.Enum):
    INVALID = "RESERVATION_DIVISION_INVALID"
    # TODO add enum values

    def to_enum(self, src):
        # TODO implement this method
        return self.INVALID


class DayOfWeek(enum.Enum):
    INVALID = "DAY_OF_WEEK_INVALID"
    SUNDAY = "DAY_OF_WEEK_SUNDAY"
    MONDAY = "DAY_OF_WEEK_MONDAY"
    TUESDAY = "DAY_OF_WEEK_TUESDAY"
    WEDNESDAY = "DAY_OF_WEEK_WEDNESDAY"
    THUESDAY = "DAY_OF_WEEK_THUESDAY"
    FRIDAY = "DAY_OF_WEEK_FRIDAY"
    SATURDAY = "DAY_OF_WEEK_SATURDAY"

    def to_enum(self, src):
        # TODO implement this method
        return self.INVALID
