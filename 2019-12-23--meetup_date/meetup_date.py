import datetime
from enum import IntEnum

class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

def meetup_date(year: int, month: int, nth: int = 4, weekday: int = 3) -> datetime.date:
    """Returns the date to hold a meetup with the given constraints

    This function examines the year and month to find the actual date
    that is the nth occurence of the given weekday (4th Thursday of the month is defualt).

    Args:
        year: year when the meetup will be held
        month: month when the meetup will be held
        nth: the nth occurence of weekday in the given year/month to use as the meetup date
            example: 2 = 2nd occurence, 1 = first occurence
        weekday: the int weekday value, where 0=Monday and 6=Sunday
            example: 4 = Friday
    Returns:
        date_of_meetup: date when meetup should be held
    Examples:
        meetup_date(2015, 8, 4, 3) returns datetime.date(2015, 8, 27) as
        the date that is the 4th Thursday (3=Thurs) in August of 2015.
    """
    # get the day of the week for the first of the year/month
    weekday_of_the_first = datetime.date(year, month, 1).weekday()

    # get days offset from the first to get the nth occurrence of weekday
    first_weekday_occurrence_offset = (weekday - weekday_of_the_first) % 7
    nth_offset = 7 * (nth - 1) # number of days to add to date to get the nth occurence of weekday

    # get the date of the month
    target_day_of_month = 1 + first_weekday_occurrence_offset + nth_offset # first of the month + offsets
    date_of_meetup = datetime.date(year,month, target_day_of_month)

    return date_of_meetup


