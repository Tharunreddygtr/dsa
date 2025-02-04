class li:
    def __init__(self, data):
        self.data = data
        self.next = None


def takeinput():
    l = [int(i) for i in input().split()]
    head = None
    tail = None
    for i in l:
        if i == -1:
            break
        else:
            l = li(i)
        if head is None:
            head = l
            tail = l
        else:
            tail.next = l
            tail = l
    return head


def printll(head):
    while head is not None:
        print(head.data, '->', end="")
        head = head.next


def insert(head, i, data):
    if i >= 0 and i <= lengthll(head):
        cur = head
        prev = None
        c = 0
        while c < i:
            prev = cur
            cur = cur.next
            c += 1
        l = li(data)
        prev.next = l
        l.next = cur
    return head


def lengthll(head):
    c = 0
    while head is not None:
        c += 1
        head = head.next
    return c


def printith(node):
    c = 0
    head = takeinput()
    while head is not None:
        if c == node:
            return head.data
        c += 1
        head = head.next


def delete(head, i):
    if i == 0:
        head = head.next
    else:
        count = 1
        temp = head
        while temp != None and count < i:
            temp = temp.next
            count += 1
        temp.next = temp.next.next
    return head


def revll(head):
    if head == None or head.next == None:
        return head
    smallhead = revll(head.next)
    cur = smallhead
    while cur.next is not None:
        cur = cur.next
    cur.next = head
    head.next = None
    return smallhead


def revll1(head, k):  # optimised solution
    i = 0
    if head == None or head.next == None:
        return head
    smallhead = revll1(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallhead

# Easy understanable solution
def revll2(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def swapll(head, node1, node2):
    i = 0
    temp = head
    if temp == None:
        return
    while temp and i < node1:
        temp = temp.next
        i += 1
    temp.data, temp.next.data = temp.next.data, temp.data


def pairwiseswapll(head):
    temp = head
    if temp == None:
        return
    while temp:
        temp.data, temp.next.data = temp.next.data, temp.data
        temp = temp.next.next


def maxdatall(head):
    max1 = head.data
    while head is not None:
        if head.data > max1:
            max1 = head.data
        head = head.next
    return max1


def middleofll(head):
    a = lengthll(head) // 2
    i = 0
    while head != None and i < a:
        head = head.next
        i += 1
    return head.data


def reverse(head, k):
    i = 0
    cur = head
    prev = None
    while i < k and cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
        i += 1
    if cur != None:
        head.next = reverse(cur, k)
    return prev


def shifting(head, m):
    cur1 = head
    cur = head
    i = 0
    while cur and i < m:
        cur = cur.next
        i += 1
    head = cur.next
    cur.next = None
    current = head
    while current.next:
        current = current.next
    current.next = cur1
    return head


def removedup(head):
    cur = head
    while cur and cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


def removeduprecu(head):
    if head == None:
        return
    if head.next != None:
        if head.data == head.next.data:
            head.next = head.next.next
            removeduprecu(head)
        else:
            removeduprecu(head.next)
    return head


def removedup_unsortedll(head):
    ptr1 = head
    while ptr1 != None and ptr1.next != None:
        ptr2 = ptr1
        while ptr2.next != None:
            if ptr1.data == ptr2.next.data:
                ptr2.next = ptr2.next.next
            else:
                ptr2 = ptr2.next
        ptr1 = ptr1.next
    return head


def ispalill(head):
    head1 = revll(head)
    while head and head1:
        if head.data != head1.data:
            return "False"
        head = head.next
        head1 = head1.next
    else:
        return "True"


head = takeinput()
print(printll(head))
print(ispalill(head))








# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def calculate(list1, list2):
    i = len(list1) - 1
    j = len(list2) - 1
    carry = 0
    sum = 0
    ten_place = 1
    while i >= 0 and j >= 0:
        cur_sum = list1[i] + list2[j] + carry
        if cur_sum > 9:
            carry = cur_sum // 10
            sum += (cur_sum % 10) * ten_place
        else:
            carry = 0
            sum += cur_sum * ten_place
        ten_place *= 10
        i -= 1
        j -= 1
    while i >= 0:
        cur_sum = list1[i] + carry
        if cur_sum > 9:
            carry = cur_sum // 10
            sum += (cur_sum % 10) * ten_place
        else:
            carry = 0
            sum += cur_sum * ten_place
        ten_place *= 10
        i -= 1

    while j >= 0:
        cur_sum = list2[j] + carry
        if cur_sum > 9:
            carry = cur_sum // 10
            sum += (cur_sum % 10) * ten_place
        else:
            carry = 0
            sum += cur_sum * ten_place
        ten_place *= 10
        j -= 1
    if carry > 0:
        sum += carry * ten_place
    return sum
def addTwoNumbers(l1, l2):
    list1 = []
    list2 = []
    current = l1
    while current:
        list1.append(current.val)
        current = current.next
    current1 = l2
    while current1:
        list2.append(current1.val)
        current1 = current1.next
    sum_value = self.calculate(list1[::-1], list2[::-1])
    prev_node = None
    head_node = None
    if sum_value == 0:
        return ListNode(0)
    while sum_value > 0:
        value = sum_value % 10
        node = ListNode(value)
        if head_node is None:
            head_node = node
        if prev_node is not None:
            prev_node.next = node
        prev_node = node
        sum_value //= 10
    return head_node


        
# simple solution compared to the above solution
def addTwoNumbers(l1, l2):
    dummy = ListNode()
    res = dummy

    total = carry = 0

    while l1 or l2 or carry:
        total = carry

        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        
        num = total % 10
        carry = total // 10
        dummy.next = ListNode(num)
        dummy = dummy.next
    
    return res.next





