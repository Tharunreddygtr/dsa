
# lifting weights 

max_capacity = 7
weights = [3, 1, 2, 10]
dp_list = [0]*len(weights)
dp_list[0] = weights[0] if weights[0] <= max_capacity else 0
# wrong answer
for i in range(1, len(weights)): 
    if dp_list[i-1] + weights[i] <= max_capacity:
        dp_list[i] = dp_list[i-1] + weights[i]
    else:
        dp_list[i] = dp_list[i-1]
print(dp_list[-1])


# right answer
def max_weight_recursive(weights, max_capacity, index=0, current_sum=0):
    if index == len(weights):
        return current_sum

    if current_sum > max_capacity:
        return 0
    exclude = max_weight_recursive(weights, max_capacity, index + 1, current_sum)
    include = 0
    if current_sum + weights[index] <= max_capacity:
        include = max_weight_recursive(weights, max_capacity, index + 1, current_sum + weights[index])
    return max(exclude, include)

# Inputs
max_capacity = 7
weights = [3, 3, 7]

# Call the recursive function
result = max_weight_recursive(weights, max_capacity)
print(result)  # Output: 7



# 0/1 knapsack problem  dp

def knapsack(wt, val, W, n):
    # Initialize the DP table
    t = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                t[i][w] = max(val[i - 1] + t[i - 1][w - wt[i - 1]], t[i - 1][w])
            else:
                t[i][w] = t[i - 1][w]

    # Backtrack to find the items that make up the maximum value
    max_profit = t[n][W]
    w = W
    items_selected = []

    for i in range(n, 0, -1):
        if max_profit <= 0:
            break
        # If the item was included, its value will be different from the value above it
        if max_profit != t[i - 1][w]:
            items_selected.append(i - 1)  # Include this item (index is 0-based)
            max_profit -= val[i - 1]  # Subtract its value from the total profit
            w -= wt[i - 1]  # Reduce the weight accordingly

    return t[n][W], items_selected

# Example usage:
profit = [6, 10, 12]
weight = [3, 2, 1]
W = 5
n = len(profit)

max_profit, items_selected = knapsack(weight, profit, W, n)
print(f"Maximum Profit: {max_profit}")
print(f"Items selected: {items_selected}")


#  recursive way
def knapsack_recursive(values, weights, W, n):
    # Base case: No items left or capacity is 0
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than the remaining capacity, exclude it
    if weights[n-1] > W:
        return knapsack_recursive(values, weights, W, n-1)
    
    # Otherwise, consider both including and excluding the nth item
    else:
        return max(
            knapsack_recursive(values, weights, W, n-1),  # Exclude the item
            values[n-1] + knapsack_recursive(values, weights, W - weights[n-1], n-1)  # Include the item
        )

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
n = len(values)

max_value = knapsack_recursive(values, weights, W, n)
print("Maximum value in knapsack:", max_value)

# house robber 198 leetcode
def rob(nums):
    length = len(nums)
    if length == 1:
        return sum(nums)
    elif length == 2:
        return max(nums[0], nums[1])
    dp = [0]*length
    dp[0] = nums[0]
    dp[1] = max(nums[1], nums[0])
    for i in range(2, length):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    return dp[length-1]
nums = [1,2,3,1]
print(rob(nums))


# min no of ways to climb the stairs either 1 or 2 at a time
def climbStairs(n):
    if n <= 3: return n

    prev1 = 3
    prev2 = 2
    cur = 0

    for _ in range(3, n):
        cur = prev1 + prev2
        prev2 = prev1
        prev1 = cur
    
    return cur



def wordBreak(s, wordDict):
    dp = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        for w in wordDict:
            start = i - len(w)
            if start >= 0 and dp[start] and s[start:i] == w:
                dp[i] = True
                break

    return dp[-1]
s = "catsand"
wordDict = ["cats","sand","cat"]
print(wordBreak(s, wordDict))
# output True
