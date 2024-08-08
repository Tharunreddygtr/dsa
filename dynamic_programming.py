
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



# 0/1 knapsack problem 

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
