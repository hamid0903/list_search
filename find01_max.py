def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """

    n=data[0]

    for i in data:
        if i>n:
            n=i
    return n
print(find_max([5,9,10,15]))
    