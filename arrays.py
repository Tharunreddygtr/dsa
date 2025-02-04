def sum_3_closest(arr, req_k):
    arr.sort()
    close_sum = float("inf")
    final_val = 0
    for i in range(len(arr)):
        j = i + 1
        k = len(arr) - 1
        while j < k:
            cur_sum = arr[i] + arr[j] + arr[k]
            current_close_sum = min(close_sum, abs(req_k - cur_sum))
            if current_close_sum < close_sum:
                close_sum = current_close_sum
                final_val = cur_sum
            if  cur_sum == req_k:
                final_val = cur_sum
                break
            elif cur_sum < req_k:
                j += 1
            else:
                k -= 1
    return final_val

print(sum_3_closest([2, 5, 6, 1, 2], 7))



def search_in_a_rotated_sorted_array():
    arr = [4, 5, 6, 7, 1, 2, 3]
    target = 6
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[left] <= arr[mid]:
            if target > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1

        elif arr[mid] >= arr[right]:
            if arr[left] > target:
                left = mid
            else:
                right = mid + 1
    return False

print(search_in_a_rotated_sorted_array())


def longestPalindrome(s):
    max1=0
    string=''
    for i in range(len(s)):
        #odd case  aba
        left=right=i
        while left>=0 and right<len(s) and s[left]==s[right]:
            if right-left+1>max1:
                max1=right-left+1
                string=s[left:right+1]
            left-=1
            right+=1
        left=i
        right=i+1
        # even case abba
        while left>=0 and right<len(s) and s[left]==s[right]:
            if right-left+1>max1:
                max1=right-left+1
                string=s[left:right+1]
            left-=1
            right+=1
    return string

# find median in sorted array in O(log(n+m)) time complexity
def findMedianSortedArrays(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    i = 0
    j = 0
    m1 = 0
    m2 = 0

    # Find median.
    for count in range(0, (n + m) // 2 + 1):
        m2 = m1
        if i < n and j < m:
            if nums1[i] > nums2[j]:
                m1 = nums2[j]
                j += 1
            else:
                m1 = nums1[i]
                i += 1
        elif i < n:
            m1 = nums1[i]
            i += 1
        else:
            m1 = nums2[j]
            j += 1

    # Check if the sum of n and m is odd.
    if (n + m) % 2 == 1:
        return float(m1)
    else:
        ans = float(m1) + float(m2)
        return ans / 2.0
print(findMedianSortedArrays([1,2], [3]))



def increasingTriplet(nums):
    first = float("inf")
    second = float("inf")
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False
nums = [1,2,3,4,5,6]
print(increasingTriplet(nums))
# output True 


# Time complexity (O(nlogn) best case and worst case O(n**2)   (not optimized)
def dailyTemperatures(temperatures):
    temp_length = len(temperatures)
    results = [0] * (temp_length)
    for index in range(temp_length):
        next_index = index + 1
        while next_index < temp_length and not temperatures[next_index]  > temperatures[index]:
            next_index +=1 
        if next_index < temp_length and temperatures[next_index]  > temperatures[index]:
            results[index] = next_index - index
        else:
            results[index] = 0
    return results
    



# Time complexity (O(n) best case and worst case O(nlogn) (optimized)
def dailyTemperatures(temperatures):
    T = len(temperatures) 
    answer = [0] * T
    stack = []
    for i in range(T):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            answer[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)            
    return answer

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))
# Output [1,1,4,2,1,1,0,0]



# Time complexity O(nlogn)
def insert(intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort()

    res = [intervals[0]]

    for i in range(1, len(intervals)):
        if res[-1][1] >= intervals[i][0]:
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])

    return res
 intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert(intervals, newInterval))



import heapq
# best case time complexity O(nlogk)
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



