#  Final Study Guide



#merge sort for array
def merge_sort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left_half = list1[:mid]
        merge_sort(left_half)
    
        right_half = list2[mid:]
        merge_sort(right_half)
    return merge(list1, left_half, right_half)




