def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """

    n=data[0]

    for i in data:
        if i%2==0:
            if i>n:
                n=i
    return n
print(find_max_even([5,20,10,12]))
