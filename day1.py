
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
        self.tail = new_node


if __name__ == "__main__":
    # create a doubly linked list to represent the dial
    L = LinkedList()
    for ii in range(0,100):
        L.append(ii)

    # connect the tail and head of the linked list
    L.tail.next = L.head
    L.head.prev = L.tail

    # read and parse document
    directions = []
    rotations = []

    file = open('day1.txt', 'r')
    lines = file.readlines()
    for line in lines:
        line.rstrip('\n')
        directions.append(line[0])
        rotations.append(int(line[1:]))

    # start dial at 50
    current_node = L.head
    for ii in range(50):
        current_node = current_node.next

    # loop through the rotations and count times dial points at 0
    password = 0
    
    for ii in range(len(rotations)):
        if directions[ii] == 'L':
            for jj in range(rotations[ii]):
                current_node = current_node.prev
                if current_node.data == 0:
                    password += 1
        else:
            for jj in range(rotations[ii]):
                current_node = current_node.next
                if current_node.data == 0:
                    password += 1

    print(password)
            


    







    

