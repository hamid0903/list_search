def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    n=data[0]

    for i in data:
        if i>n:
            n=i
    
    k=data[0]

    for j in data:
        if i<k:
            k=j
    return n+k 


print(find_max_min_sum([5,15,6,15,7,9]))
