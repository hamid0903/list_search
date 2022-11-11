def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    n=data[0]

    for i in data:
        if i%2==1:
            if i<n:
                n=i
    return n
print(find_min_odd([5,9,10,12]))

