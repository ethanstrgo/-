# def quick_sort1(seq):
##第一种
#     if seq == []:
#         return []
#     else:
#         pivot = seq[0]
#         lesser = quick_sort1([x for x in seq[1:] if x < pivot])
#         greater = quick_sort1([x for x in seq[1:] if x >= pivot])
#         return  lesser + [pivot] + greater
# if __name__ == '__main__':
#     seq = [3,41,532,2132,4,453,32,55,7,42]
#     print(quick_sort1(seq))

def quick_sort2(lists, left, right):
# 第二种
    if left >= right:
        return  lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort2(lists, low, left -1)
    quick_sort2(lists, left + 1, high)
    return lists
if __name__ == '__main__':
    seq = [3,41,532,2132,4,453,32,55,7,42]
    print(quick_sort2(seq, 0, 9))
