class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data): # add a new node to the end of the list
        last = Node(data) # get a new node by calling the Node class to create an instance
        if self.head is None: # if list is empty, assign the new node as the head node
            self.head = last
            return

        this_node = self.head

        while (this_node.next):
            this_node = this_node.next # point the new node to the next one

        this_node.next = last # put the data in the new node at the end of the list

    def prepend(self, data): # add a new node to the beginning of the list
        first = Node(data) # get a new node by calling the Node class to create an instance
        if self.head is None: # if list is empty, assign the new node as the head node
            self.head = first
            return
        else:
            first.next = self.head # assign the new node as the head node
            self.head = first # put the data in the new node at the beginning of the list

    def print_list(self):
        this_node = self.head # point to the head node
        while (this_node):
            print(this_node.data)
            this_node = this_node.next # point to the next node

# create a new linked list
x = LinkedList()

# add nodes to the linked list
x.prepend('g')
x.append('a')
x.append('b')
x.prepend('c')
x.append('d')

# print the linked list
print('List contents:')
x.print_list()