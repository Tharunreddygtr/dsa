
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
