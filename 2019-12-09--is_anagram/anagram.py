def get_char_frequency_dict(word):
    """returns a dict mapping chars present word to the count of those chars

    Args:
        word - the string to process into a character frequency dict
    
    Returns:
        dict(char->count) - e.g. "egg" returns {'e': 1, 'g': 2}
    """
    freq_dict = {}
    for char in word:
        freq_dict.setdefault(char, 0)
        freq_dict[char] += 1

    return freq_dict


def is_anagram(word1, word2):
    """ return true if word1 is an anagram of word2

    Checks if word1 and word2 are anagrams, without concern for 
    whitespace or case. If they are anagrams, True is returned, otherwise False.

    Args:
        word1 - first string to compare
        word2 - second string to compare
    
    Returns:
        boolean - true if word1 and word2 are anagrams, false if not
    """
    # get character frequency dicts for faster comparisons
    frequency_dict_1 = get_char_frequency_dict(word1.lower())
    frequency_dict_2 = get_char_frequency_dict(word2.lower())

    return frequency_dict_1 == frequency_dict_2