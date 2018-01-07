def binary_serach(list, item):
    lower, upper = 0, len(list)-1
    while lower <= upper:
        middle = (lower + upper) // 2
        if list[middle] == item:
            return middle
        if list[middle] > item :
            upper = middle - 1
        else:
            lower = middle + 1
    return None
print(binary_serach(list(range(1, 100)), 88))
