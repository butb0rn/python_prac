class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

def partition_list(list_item, key):
    node = list_item.head
    before_start = Node(None)
    before_end  = Node(None)
    after_start  = Node(None)
    after_end = Node(None)

    while node is not None:
        if node.data < key:
            if before_start.data is None:
                before_start = node
                before_end   = before_start
            else:
                before_end.next = node
                before_end = node
        else:
            if after_start.data is None:
                after_start = node
                after_end = after_start
            else:
                after_end.next = node
                after_end = node

        node = node.next

    before_end.next = after_start

    while before_start is not None:
       print before_start.data
       before_start = before_start.next





mylist = LinkedList()
mylist.add(12)
mylist.add(8)
mylist.add(1)
mylist.add(3)
mylist.add(6)
mylist.add(9)
mylist.add(13)
mylist.add(0)
mylist.add(6)
mylist.add(19)
mylist.add(5)
mylist.add(5)
partition_list(mylist, 6)
