def count(s):
    """
    Count the occurences of each character in a string.

    Args: 
        s (str): The input string.

    Returns:
        dict: A diction where keys are the characters and values are the count.

    Example:
        >>> count("aab")
        {'a': 2, 'b': 1}
    """

    result = {}
    for letter in s:
        if letter not in result:
            result[letter] = s.count(letter)
            s = [item for item in s if item != letter]
    return result
