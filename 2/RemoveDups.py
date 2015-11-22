class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next_data = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_data

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next_data = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp


def remove_dups(head):
    current_node = head.head
    while current_node is not None:
        next_node = current_node
        while next_node.get_next() is not None:
            if next_node.get_next().get_data() == current_node.get_data():
                next_node.set_next(next_node.get_next().get_next())
            else:
                next_node = next_node.get_next()

        current_node = current_node.get_next()


    res = head.head
    while res is not None:
        print res.get_data()
        res = res.get_next()


mylist = LinkedList()
mylist.add(31)
mylist.add(31)
mylist.add(31)
mylist.add(31)
mylist.add(77)
mylist.add(26)
mylist.add(54)
mylist.add(17)
mylist.add(17)
mylist.add(17)
mylist.add(93)
mylist.add(1)
mylist.add(26)
mylist.add(54)

remove_dups(mylist)
