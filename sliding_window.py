
def minSwaps(nums):
    total = sum(nums)  # Total number of 1's in the array
    n = len(nums)

    # If there are no 1's, no swaps are needed
    if total == 0:
        return 0

    # Extend the array to handle the circular nature
    nums *= 2

    # Initialize the sliding window
    window_sum = sum(nums[:total])
    max_ones = window_sum
    swaps = total - max_ones

    for i in range(1, n):
        # Update the number of 1's in the current window by sliding the window
        window_sum += nums[i + total - 1] - nums[i - 1]
        max_ones = max(max_ones, window_sum)
        swaps = min(swaps, total - max_ones)

    return swaps


nums = [0, 1, 0, 1, 1, 0, 0]
print(minSwaps(nums))
