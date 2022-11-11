def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    idx=0
    m=data[idx]

    for i in range(len(data)):
        if data[i]<m:
            m=data[i]
            idx=i
    return idx

print(find_min_index([5,7,1,15,6,4]))

