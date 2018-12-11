from random import shuffle

class RandomNumberGenerator():
    """
    RandomNumberGenerator is designed to:
    - provide random integer numbers in a range between min (inclusive) and max (exclusive)
    - never repeats a value in the range until all values have been seen once
    - allow for ad-hoc range editing while respecting the need to not repeat values
    """
    def __init__(self, range_min=0, range_max=10):
        # validate min/max
        if(range_min >= range_max): raise ValueError("min must be less than max")

        # instantiate
        self._min = range_min
        self._max = range_max
        
        # generate the random values list
        self._values = self.getRandomValues(range_min, range_max)
    
    def getRandomValues(self, `minVal, maxVal):
        values = [i for i in range(minVal, maxVal)]
        return shuffle(values)
        
