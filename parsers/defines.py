from enum import Enum


# An enum of semester
class Semester(Enum):
    FIRST_TERM = 1
    SECOND_TERM = 2
    MID_TERM = 3

    def to_raw(self) -> int:
        if self == self.FIRST_TERM:
            return 3
        elif self == self.SECOND_TERM:
            return 12
        elif self == self.MID_TERM:
            return 16

    @staticmethod
    def from_raw(raw: str):
        if raw == '3':
            return Semester.FIRST_TERM
        elif raw == '12':
            return Semester.SECOND_TERM
        elif raw == '16':
            return Semester.MID_TERM
        else:
            raise Exception('Invalid semester valid given.')
