class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.Next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp


def is_palindrome(linkedList):
    slow = linkedList.head
    fast = linkedList.head
    stack = []

    while (fast is not None) and (fast.next is not None):
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast is not None:
        slow = slow.next

    while slow is not None:
        if slow.data != stack.pop():
            return False
        slow = slow.next
    return True


mylist = LinkedList()
mylist.add(0)
mylist.add(1)
mylist.add(1)
mylist.add(3)
mylist.add(6)
mylist.add(1)
mylist.add(1)
mylist.add(0)


print is_palindrome(mylist)
