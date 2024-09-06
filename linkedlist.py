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
