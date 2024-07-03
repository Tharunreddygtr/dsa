list1 = [10, 9, 7, 18, 13, 19, 4, 20, 21, 14]
even = []
odd = []
for i in list1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
output = [0] * len(list1)
i = 0
j = 0
for index, value in enumerate(output):
    if index % 2 == 0:
        output[index] = even[i]
        i += 1
    else:
        output[index] = odd[j]
        j += 1
# print(output)
# print("one method")
even_index = 0
odd_index = 1
while even_index < odd_index and odd_index < len(list1):
    if list1[even_index] % 2 != 0 and list1[odd_index] % 2 == 0:
        list1[even_index], list1[odd_index] = list1[odd_index], list1[even_index]
        even_index += 2
        odd_index += 2
    elif list1[even_index] % 2 != 0:
        odd_index += 2
    elif list1[odd_index] % 2 == 0:
        even_index += 2
    else:
        odd_index += 2
        even_index += 2
        # 3 6 12 1 5 8


# print(list1)
def maximum_profit(arr):
    profit = 0
    i = 0
    while i < len(arr) - 1:
        # day to buy the stock
        while i < len(arr) - 1 and arr[i + 1] <= arr[i]:
            i += 1
        if i == len(arr) - 1:
            print("unable to make profit")
            break
        buy = i
        i += 1
        # day to sell the stock
        while i < len(arr) - 1 and arr[i + 1] > arr[i]:
            i += 1
        sell = i
        profit += arr[sell] - arr[buy]
        print("buy day", buy)
        print("sell day", sell)
    print(profit)


arr = [100, 180, 260, 310, 40, 535, 695]


# maximum_profit(arr)
def infixToPostix(string):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    operators = "+-*/^()"
    output = ""
    stack = []
    for i in string:
        if i not in operators:
            output += i
            # print(output)
        elif i == "(":
            stack.append(i)
        elif i == ")":
            while stack and stack[-1] != "(":
                output += stack.pop()
            stack.pop()
            # print(output)
        else:
            while stack and stack[-1] != "(" and precedence[i] <= precedence[stack[-1]]:
                output += stack.pop()
            stack.append(i)
            # print(output)
    while stack:
        output += stack.pop()
    # print(output)


#  mn*pq-+r+
string = "m*n+(p-q)+r"


# infixToPostix(string)
def infixtoPrefix(string):
    string1 = string[::-1]
    operators = "+-*/^()"
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    output = ""
    stack = []
    for i in string1:
        if i not in operators:
            output += i
            print(output)
        elif i == ")":
            stack.append(i)
            print(output)
        elif i == "(":
            while stack and stack[-1] != ")":
                output += stack.pop()
            stack.pop()
            print(output)
        else:
            if i == "^":
                while stack and stack[-1] != ")" and i == "^":
                    output += stack.pop()
                stack.append(i)
                print(output)
            else:
                while stack and stack[-1] != ")" and precedence[stack[-1]] > precedence[i]:
                    output += stack.pop()
                stack.append(i)
                print(output)
    while stack:
        output += stack.pop()
    print(output[::-1])


# infixtoPrefix(string)
nums = [1, 2, 3, 4, 4, 5, 6, 7, 8, 10, 12, 4, 2, 1]
# 1 1 2 2 3 4 4 4 5 6 7 8 10 12
target = 10
nums.sort()
list1 = []
for i in range(len(nums) - 2):
    j = i + 1
    k = len(nums) - 1
    while j < k:
        list = [nums[i], nums[j], nums[k]]
        if sum(list) == target:
            list1.append(list)
        elif sum(list) < target:
            j += 1
        else:
            k -= 1


# print(list1)
# nums=[1,2,3,4,5,6,7,8]
# target=5
# start=0
# end=len(nums)-1
# while start<end:
#     mid=(start+end)//2
#     if target==nums[mid]:
#         print(mid)
#     elif target<nums[mid]:
#         end=mid
#     else:
#         start=mid
class linkedlist:
    def __init__(self, data):
        self.data = data
        self.next = None

    def revknodes(self, head, k):
        prev = None
        cur = head
        i = 0
        while cur and i < k:
            next1 = cur.next
            cur.next = prev
            prev = cur
            cur = next1
            i += 1
        if cur.next != None:
            cur.next = linkedlist.revknodes(self, cur.next, k)
        else:
            return prev

    def printll(self, head):
        cur = head
        while cur:
            print(cur.data, end="->")
        print(None)


head = linkedlist(5)
head.next = linkedlist(6)
head.next.next = linkedlist(7)
head.next.next.next = linkedlist(8)
head.next.next.next.next = linkedlist(9)
head.next.next.next.next.next = linkedlist(10)
head1 = linkedlist.revknodes(head, 3)
linkedlist.printll(head1)
# print(int("FF", 16))


def spiralOrder(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)
        matrix = (list(zip(*matrix)))[::-1]
    return res


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiralOrder(matrix1))

def spiralOrder(matrix):
    res = []
    round = 1
    while matrix and matrix[0]:
        if round == 1:
            res.extend(matrix.pop(0))
            round += 1
        elif round == 2:
            for i in matrix:
                res.append(i.pop())
            round += 1
        elif round == 3:
            res.extend(matrix.pop(-1)[::-1])
            round += 1
        elif round == 4 and len(matrix[0]):
            for i in matrix[::-1]:
                res.append(i.pop(0))
            round = 1
    return res


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiralOrder(matrix1))
