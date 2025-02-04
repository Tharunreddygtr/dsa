def maxSubArray(nums):
    max_sub_array = float("-inf")
    current_sub_array = 0
    for num in nums:
        current_sub_array += num
        max_sub_array = max(current_sub_array, max_sub_array)
        if current_sub_array < 0:
            current_sub_array = 0

    return max_sub_array
nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# maximum product sub array
def maxProduct(self, nums):
    if not nums:
        return 0
    max_prod = prev_max = prev_min =  nums[0] 
    for i in range(1, len(nums)): 
        curr_min = min(prev_max * nums[i], prev_min * nums[i], nums[i]) 
        curr_max = max(prev_max * nums[i], prev_min * nums[i], nums[i])
        prev_min, prev_max = curr_min, curr_max
        max_prod = max(curr_max, max_prod)    
    return max_prod

		
