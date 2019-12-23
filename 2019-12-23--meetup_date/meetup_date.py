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
            example: -1 = last occurence in the month, -2 = 2nd to last occurence in the month
            example: 0 = not acceptable input
        weekday: the int weekday value, where 0=Monday and 6=Sunday
            example: 4 = Friday
    Returns:
        date_of_meetup: date when meetup should be held
    Examples:
        meetup_date(2015, 8, 4, 3) returns datetime.date(2015, 8, 27) as
        the date that is the 4th Thursday (3=Thurs) in August of 2015.
    """
    # check args
    if nth is 0:
        raise ValueError("nth arg cannot be 0")

    # get an anchor date, being the first of the current or next month, to add or subtract
    # days to/from to get the meetup date
    anchor_month = month if nth > 0 else month + 1
    anchor_year = year
    if anchor_month > 12:
        anchor_month = 1
        anchor_year += 1
    anchor_date = datetime.date(anchor_year, anchor_month, 1)

    # get days offset from the first to get the nth occurrence of weekday
    first_weekday_occurrence_offset = (weekday - anchor_date.weekday()) % 7
    nth_offset = 7 * (nth - 1) if nth > 0 else 7*nth

    # get the date of the month by moving days_offset days from the anchor date
    days_offset = first_weekday_occurrence_offset + nth_offset
    date_of_meetup = anchor_date + datetime.timedelta(days=days_offset)

    return date_of_meetup


