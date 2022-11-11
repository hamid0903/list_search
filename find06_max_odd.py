def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    n=data[0]

    for i in data:
        if i%2==1:
            if i>n:
                n=i
    return n
print(find_max_odd([5,9,11,12]))