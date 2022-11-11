def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    n=data[0]

    for i in data:
        if i%2==0:
            if i<n:
                n=i
    return n
print(find_min_even([5,9,10,12]))

