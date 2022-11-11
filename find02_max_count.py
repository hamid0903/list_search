from find01_max import find_max


def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    n=data[0]
    
    for i in data:
        if i>n:
            n=i
    k=0
    for i in data:
        if n==i:
            k+=1    
    return k

print(find_max_count([5,15,6,15,7,9]))
