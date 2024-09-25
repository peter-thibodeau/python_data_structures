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

    def prepend(self, data):  # add a new node to the beginning of the list
        first = Node(data)  # get a new node by calling the Node class to create an instance
        if self.head is None:  # if list is empty, assign the new node as the head node
            self.head = first
            return
        else:
            first.next = self.head # assign the new node as the head node
            self.head = first  # put the data in the new node at the beginning of the list

    def remove_node(self, data): # remove first node with supplied data
        this_node = self.head # assign the new node as the head node

        if this_node.data == data: # if the node contains the supplied data
            if (self.head == None): # if the node is not the head node
                return

            self.head = self.head.next # put the node after the head

            return

        while (this_node != None and this_node.next.data != data):
            this_node = this_node.next # move to the next point

        if this_node == None: # there is no node in the list with the supplied data
            return
        else:
            this_node.next = this_node.next.next # point to the node with the supplied data

    def print_list(self):
        this_node = self.head # point to the head node
        while (this_node):
            print(this_node.data)
            this_node = this_node.next # point to the next node

x = LinkedList()

x.prepend('a')
x.append('b')
x.prepend('c')
x.append('d')
x.remove_node('c')
x.prepend('e')

print("Contents of linked list:")
x.print_list()