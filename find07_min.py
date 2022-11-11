def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """

    n=data[0]

    for i in data:
        if i<n:
            n=i
    return n
print(find_min([5,9,10,15]))