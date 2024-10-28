# 1. Sliding Window Pattern
# Used for problems involving contiguous subarrays or substrings. The window slides over the data to find a specific result.

# Example: Finding the maximum sum of a subarray of size k.
# python

def max_sum_subarray(arr, k):
    max_sum, window_sum = 0, 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if i >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[i - (k - 1)]
    return max_sum
# 2. Two Pointers Pattern
# Used for problems that involve pairs in an array or a linked list. Two pointers are used to iterate through the data structure.

# Example: Finding if there exist two elements in a sorted array that sum up to a given target.
# python

def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return False
# 3. Fast and Slow Pointers (Tortoise and Hare)
# Used for problems involving cyclic patterns in linked lists or arrays.

# Example: Detecting a cycle in a linked list.
# python

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
# 4. Merge Intervals Pattern
# Used for problems involving merging overlapping intervals.

# Example: Merging overlapping intervals.
# python

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
# 5. Cyclic Sort Pattern
# Used for problems involving sorting a sequence of numbers where each number is in a known range.

# Example: Finding the missing number in an array of consecutive numbers from only  0 to n numbers.
# python

def find_missing_number(arr):
    i, n = 0, len(arr)
    while i < n:
        j = arr[i]
        if arr[i] < n and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i] 
            # ensure that arr[i] corresponds to i ex:- 1 value should be in 1's index and 4 value should be in 4th index.
        else:
            i += 1
    for i in range(n):
        if arr[i] != i:
            return i
    return n

# 2th method use sum of n natural numbers formula    n(n+1)/2  subtract the given array sum gets the missing value.


# 6. Topological Sort Pattern
# Used for problems involving scheduling or ordering of tasks.

# Example: Course Schedule problem (determining if you can finish all courses given prerequisites).
# python

from collections import defaultdict, deque

def can_finish_courses(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = {i: 0 for i in range(numCourses)}
    
    for dest, src in prerequisites:
        graph[src].append(dest)
        indegree[dest] += 1
    
    queue = deque([k for k in indegree if indegree[k] == 0])
    visited = 0
    
    while queue:
        course = queue.popleft()
        visited += 1
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return visited == numCourses
# 7. Binary Search Pattern
# Used for problems that involve finding an element in a sorted array or search space.

# Example: Finding the first bad version in a sequence of versions.
# python

def first_bad_version(n, isBadVersion):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left
# 8. Backtracking Pattern
# Used for problems that involve searching for a solution in a state space tree.

# Example: Solving the N-Queens problem.
# python

def solve_n_queens(n):
    def is_not_under_attack(row, col):
        for prev_row in range(row):
            if queens[prev_row] == col or \
               queens[prev_row] - prev_row == col - row or \
               queens[prev_row] + prev_row == col + row:
                return False
        return True

    def place_queen(row):
        if row == n:
            result.append(queens[:])
            return
        for col in range(n):
            if is_not_under_attack(row, col):
                queens[row] = col
                place_queen(row + 1)
                queens[row] = -1

    result = []
    queens = [-1] * n
    place_queen(0)
    return result
# 9. Dynamic Programming Pattern
# Used for problems that can be broken down into overlapping subproblems with optimal substructure.

# Example: Finding the length of the longest increasing subsequence.
# python

def length_of_lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
# 10. Greedy Pattern
# Used for problems that require making the locally optimal choice at each stage.

# Example: Finding the minimum number of coins for a given amount.
# python

def min_coins(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count if amount == 0 else -1
# These patterns are fundamental to solving various types of problems in data structures and algorithms efficiently.
#       Understanding and applying these patterns can greatly enhance your problem-solving skills.
