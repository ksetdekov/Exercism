def filter_list(x):
    """return a new list with the strings filtered out"""

    return [i for i in x if isinstance(i, int) and i >= 0]
