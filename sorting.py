
# recursive way
quick_sort = [4, 5, 3, 2, 7, 9, 1]


def quick_sort_fun(quick_sort):
    if not quick_sort:
        return []
    mid = quick_sort[0]
    left_list = [i for i in quick_sort if i < mid]
    right_list = [i for i in quick_sort if i > mid]

    return quick_sort_fun(left_list) + [mid] + quick_sort_fun(right_list)


print(quick_sort_fun(quick_sort))
# time complexity O(nlog(n))        
