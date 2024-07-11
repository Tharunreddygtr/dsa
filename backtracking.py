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
