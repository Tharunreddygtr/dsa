def combinationSum3(k, n):
    list1 = []
    output = []

    def backtracking(number):
        if len(list1) > k:
            return
        if sum(list1) == n and len(list1) == k:
            output.append(list1.copy())
            return
        for i in range(number, 10):
            list1.append(i)
            backtracking(i + 1)
            list1.pop()

    backtracking(1)
    return output


print(combinationSum3(9, 45))

def permute(nums):
    output_list = []

    def backtrack(i):
        if i == len(nums) - 1:
            output_list.append(nums[:])
            return
        for j in range(i, len(nums)):
            temp = nums[i]
            temp2 = nums[j]
            nums[i], nums[j] = nums[j], nums[i]
            backtrack(i+1)
            nums[i] = temp
            nums[j] = temp2

    backtrack(0)
    return output_list


nums = [1, 2, 3]
print(permute(nums))
