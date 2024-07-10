
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


# merger sort

def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point to divide the array into two halves
        mid = len(arr) // 2

        # Divide the array elements into 2 halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the first half
        merge_sort(left_half)

        # Recursively sort the second half
        merge_sort(right_half)

        # Initialize pointers for left_half, right_half, and the main array
        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
