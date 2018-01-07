def insert_sort(lists):
    #插入排序
    '''
   '稳定的排序方法
    算法适用于少量数据的排序
    时间复杂度为O(n^2)
    '''

    count = len(lists)
    for i in  range(1, count):
        l = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > lists[i]:
                lists[j + 1] = lists[j]
                lists[j] = l
            j -= 1
            i -= 1
    return  lists
print(insert_sort([3, 54, 64, 123, 453, 2, 32]))
