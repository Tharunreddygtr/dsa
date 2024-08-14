
# lifting weights 

max_capacity = 7
weights = [3, 1, 2, 10]
dp_list = [0]*len(weights)
dp_list[0] = weights[0] if weights[0] <= max_capacity else 0
for i in range(1, len(weights)):
    if dp_list[i-1] + weights[i] <= max_capacity:
        dp_list[i] = dp_list[i-1] + weights[i]
    else:
        dp_list[i] = dp_list[i-1]
print(dp_list[-1])



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

