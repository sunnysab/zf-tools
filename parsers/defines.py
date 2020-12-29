from enum import Enum


# A class of School year
class SchoolYear:
    ALL = None
    __year = None

    def __init__(self, year: int = ALL):
        self.__year = year

    def __str__(self) -> str:
        if self.__year is not None:
            return str(self.__year)
        else:
            return ''


class AllSchoolYear(SchoolYear):
    def __init__(self):
        super().__init__()


# An enum of semester
class Semester(Enum):
    ALL = 0
    FIRST_TERM = 1
    SECOND_TERM = 2
    MID_TERM = 3

    def to_raw(self) -> str:
        if self == self.ALL:
            return ''
        elif self == self.FIRST_TERM:
            return '3'
        elif self == self.SECOND_TERM:
            return '12'
        elif self == self.MID_TERM:
            return '16'

    @staticmethod
    def from_raw(raw: str):
        if raw == '':
            return Semester.ALL
        elif raw == '3':
            return Semester.FIRST_TERM
        elif raw == '12':
            return Semester.SECOND_TERM
        elif raw == '16':
            return Semester.MID_TERM
        else:
            raise Exception('Invalid semester valid given.')
