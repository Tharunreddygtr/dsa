# practising
class LinkedList:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class Linked_list_methods:
    def takeinput(self):
        l = [int(i) for i in input().split()]
        head = None
        tail = None
        for i in l:
            if i == -1:
                break
            else:
                li = LinkedList(i)
                if head is None:
                    head = li
                    tail = li
                else:
                    tail.next = li
                    tail = tail.next
        return head

    def print_ll(self, head):
        cur = head
        while cur:
            print(cur.data, end="->")
            cur = cur.next
        print(None)

    def rev_ll(self, head):
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def rev_pair(self, head):
        cur = head
        while cur and cur.next:
            cur.data, cur.next.data = cur.next.data, cur.data
            cur = cur.next.next
        return head

    def lengthll(self, head):
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        return length

    def insert(self, node, position, head):
        node1 = LinkedList(node)
        if position == 0:
            node1 = LinkedList(node)
            node1.next = head
            return node1
        else:
            cur = head
            position = 1
            while cur and position > 1:
                position -= 1
                cur = cur.next
            nxt = cur.next
            cur.next = node1
            node1.next = nxt
            return head

    def swap(self, node1, node2, head):
        i = 0
        cur = head
        swap1 = None
        swap2 = None
        while cur and i < obj.lengthll(head):
            if i == node1:
                swap1 = cur
            if node2 == i:
                swap2 = cur
            cur = cur.next
            swap1.data, swap2.data = swap2.data, swap1.data
        return head


obj = Linked_list_methods()
head = obj.takeinput()
obj.print_ll(head)
head = obj.rev_pair(head)
head = obj.swap(0, 2, head)
obj.print_ll(head)
