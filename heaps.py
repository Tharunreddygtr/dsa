import heapq

def kSmallestPairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []

    heap = []
    result = []

    # Initialize the heap with (sum, index1, index2)
    for i in range(min(k, len(nums1))):  # Only first k elements from nums1
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

    while k > 0 and heap:
        _, i, j = heapq.heappop(heap)  # Pop the smallest sum pair
        result.append((nums1[i], nums2[j]))

        # If there's a next element in nums2, push (sum, i, j+1)
        if j + 1 < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        k -= 1

    return result


# Example usage
nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3
print(kSmallestPairs(nums1, nums2, k))


def findKthLargest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

    return heap[0]
nums = [72, 2, 3, 4]
k = 2
print(findKthLargest(nums, k))
