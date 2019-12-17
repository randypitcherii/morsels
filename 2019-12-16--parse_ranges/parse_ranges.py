def parse_ranges(ranges_string):
    """ parses string of ranges and returns parsed iterable

    Args:
        ranges_string - string containing series of ranges to parse
            e.g. '1-4,6-6,43-45'
    Returns:
        iterable parsed from the ranges_string
            e.g. [1,2,3,4,6,43,44,45]
    """
    # process input into list of range start/stops
    list_of_range_strings = ranges_string.split(',')
    ranges = []
    for range_string in list_of_range_strings:
        start, stop = range_string.split('-')
        ranges.append((int(start), int(stop)))
    
    # build the iterable
    parsed_ranges = []
    for start, stop in ranges:
        while start <= stop:
            parsed_ranges.append(start)
            start += 1
    
    return parsed_ranges

