
# node class would point to which node it's going next
class node:

#   initial constructor contains the variables to start off with which are
#   value and link

# preconditions:  it sets the value of node and takes link 
# postconditions: nothing
# complexity: O(1) in all case
    def __init__(self,value,link=None):
        self.value = value
        self.next = link

#   string format which is as below in the function in the time of printing
# preconditions:  it takes nothing
# postconditions: The output would be the structure of the printed string
# complexity: O(1) in all case
    def __str__(self):
        return "{"+str(self.value)+"}"

class linkedList:

    # preconditions:  it sets the value of head node and counter 
# postconditions: nothing
# complexity: O(1) in all case
    def __init__(self):
        self.head = None
        self.count = 0

#   string format which is as below in the function in the time of printing
# preconditions:  It takes nothing
# postconditions: The output would be the count of number of string
# complexity: O(n) in all case
    def __len__(self):
        return self.count

#   This method checks in case the list is empty, if it
#   does then it sets the length to 0
 # preconditions:   It checks the length of linked list
# postconditions: The output would be the length of array if it's zero
# complexity: O(n) in all case
    def is_empty(self):
        return self.count == 0

#   string format which is as below in the function in the time of printing
# preconditions:  The method takes nothing
# postconditions: The output would be the structure of the printed string
# complexity: O(n) in all case
    def __str__(self):
        string = "List: (" + str(len(self)) + ") "
        current = self.head
        while not (current is None):
            string += " -> " + str(current)
            current = current.next
        string += ""
        return string

#   It would use the node from that class and link the arrow to next node
# preconditions:  The method takes the index
# postconditions: The output would be the current node
# complexity: O(n) in all case

    def _get_node(self,index):

        current = self.head
        if index >= len(self) or index < 0:
            raise StopIteration("Node doesn't exist at this index")
        currentPos = 0
        while not current is None and currentPos < index:
            current = current.next
            currentPos += 1
        return current

#   In insert method, the node would be put in between others and will have the arrow set
#   these are getting inserted by both positive and negative(it's automatically set to 0) values of index
# preconditions:   It takes the index and item in
# postconditions: The output would be node will be inserted according to it's index
# complexity: O(n) in all case
    def insert(self,item,index):
        if index<0:
            index=0
        elif index>len(self):
            index=len(self)

        if index==0:
            self.head = node(item,self.head)
        else:
            Node = self._get_node(index-1)
            Node.next = node(item, Node.next)
        self.count+=1

#   Delete will remove the node in the list if the index of the item is
#   in the list
# preconditions:  It takes the index in
# postconditions: The output would include the item removed from the index given in the input or else it will raise IndexError
# complexity: O(n) in all case
    def delete(self,index):
        if self.is_empty():
            raise IndexError("The list is empty")
        if index<0 or index>=len(self):
            raise IndexError("Index is out of range")

        if index==0:
            self.head = self.head.next
        else:
            Node = self._get_node(index - 1)
        #    itemToRemove = Node.next
         #   Node.next = itemToRemove.next
            Node.next=Node.next.next
        self.count-=1

def LinkedList():

    a_list = linkedList()
    a_list.insert(5,0)
    a_list.insert('Hello',3)
    a_list.insert(10,2)
    print(a_list)
    #print(len(a_list.array))
    a_list.delete(1)
    #print(a_list[-1,5])
    print(a_list)

    b_list = linkedList()
    b_list.insert(21,1)
    b_list.insert(2,3)
    b_list.insert(2,0)
    b_list.insert(121,4)
    print(b_list)
LinkedList()


