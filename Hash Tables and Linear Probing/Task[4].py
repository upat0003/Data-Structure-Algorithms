import ctypes


def build_array(size):
    """
    This function creates an array of references to Python Objects.
    Args:
        size (int): A positive integer, the size of the array.
    Returns:
        An array of python references with the given size.
    """
    if size <= 0:
        raise ValueError("Array size should be larger than 0.")
    if not isinstance(size,  int):
        raise ValueError("Array size should be an integer.")
    array = (size * ctypes.py_object)()
    array[:] = size * [None]
    return array




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




class SeperateChaining:

    # preconditions:  it sets the value of head node and counter 
# postconditions: nothing
# complexity: O(1) in all case
    def __init__(self, a=101, size=400000):
        self.table_size = size
        self.head = None
        self.count = 0
        self.a = a
        self.array = build_array(self.table_size)
        self.collisions = 0
        self.probe_length = 0


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



    def _hash_value(self, key):
         
        """
                        Functionality: to find hash values
                        Precondition: works on provided values of a, the base
                        Post-condition: none
                        Error handling: none
                        Time complexity: O(N)
                        Space complexity: O(1)
                        Return Value: h, the hash value
                        Parameters: key
                        Arguments: a, h
        """
        a=97
                       
        h = 0
        for c in key:
            h = (h * a + ord(c)) % self.table_size
        return h

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
            Nod
            e.next=Node.next.next
        self.count-=1

    def __setitem__(self, key, value):
        """
                            Functionality: to set a certain value as an item in the hash table
                            Precondition: none
                            Post-condition: none
                            Error handling: raises index error if there is not enough space in the table for storage
                            and goes to index 0 if end of list is reached
                            Time complexity: O(N)
                            Space complexity: O(1)
                            Return Value: none
                            Parameters: key, value
                            Arguments: position, array[position], count
                """
        position = self._hash_value(key)

        if self.array[position] is not None:
            self.collisions += 1

        for _ in range(self.table_size):
            self.probe_length += 1
                # If there is nothing stored at the position
            if self.array[position] is None:
                self.array[position] = (key, value)
                self.count += 1
                return

                # If found key
            elif self.array[position][0] == key:
                self.array[position] = (key, value)
                return

                # Store in next position if current position is already being used
            else:
                position = (position+1) % self.table_size
                if position >= self.table_size:
                    position = 0

        self.rehash(key)
        self.__setitem__(key, value)

    def rehash(self, key):
        """
                                Functionality: to find hash value again
                                Precondition: works on provided values of a, the base
                                Post-condition: none
                                Error handling: none
                                Time complexity: O(N)
                                Space complexity: O(1)
                                Return Value: position in the hash table
                                Parameters: key
                                Arguments: position
                        """

        position = self._hash_value(key)
        return position

    def __getitem__(self, key):
        """
                            Functionality: to get a certain item from the table using its key
                            Precondition: none
                            Post-condition: none
                            Error handling: raises error if key not found in the table
                            Time complexity: O(N)
                            Space complexity: O(1)
                            Return Value: self.array[position][1]
                            Parameters: key
                            Arguments: position
                """
        position = self._hash_value(key)
        for _ in range(self.table_size):

            if self.array[position] is None:
                raise KeyError(key)

            elif self.array[position][0] == key:
                return self.array[position][1]

            else:
                # There is something there, but different key
                position = (position+1) % self.table_size
                if position >= self.table_size:
                    position = 0
        raise KeyError(key)


    def __contains__(self, key):
        """
                            Functionality: to check if the table contains a certain key
                            Precondition: none
                            Post-condition: none
                            Error handling: none
                            Time complexity: O(N)
                            Space complexity: O(1)
                            Return Value: True or False
                            Parameters: key
                            Arguments: none
                """
        for _ in range(self.count):
            if key in self:
                return True
            else:
                return False
        

if __name__ == "__main__":
    import timeit
    my_table = SeperateChaining()

    file1 = open('english_large.txt')

    start = timeit.default_timer()
    for line in file1:
        item = file1.readline()
        my_table[line] = item

    end = timeit.default_timer()



    print("Time taken to read english_large is:", end - start, "seconds.")
    print("Number of collisions are:", my_table.collisions)
    print("The probe length is:", my_table.probe_length)
    print("Average probe length is:", my_table.probe_length/my_table.count, "\n")


 # Reading second file
    file2 = open('english_small.txt')

    start = timeit.default_timer()
    for line in file2:
        item = file2.readline()
        my_table[line] = item

    end = timeit.default_timer()

    print("Time taken to read english_small is:", end - start, "seconds.")
    print("Number of collisions are:", my_table.collisions)
    print("The probe length is:", my_table.probe_length)
    print("Average probe length is:", my_table.probe_length / my_table.count, "\n")

    # Reading third file
    file3 = open('french.txt')

    start = timeit.default_timer()
    for line in file3:
        item = file3.readline()
        my_table[line] = item

    end = timeit.default_timer()

    print("Time taken to read french is:", end - start, "seconds.")

    print("Number of collisions are:", my_table.collisions)
    print("The probe length is:", my_table.probe_length)
    print("Average probe length is:", my_table.probe_length / my_table.count, "\n")




'''

For a=108 and tablesize=400000

[Linear probing]

Time taken to read english_large is: 0.6250387963942574 seconds.
Number of collisions are: 44558
The probe length is: 186698
Average probe length is: 1.9204254399950627 

Time taken to read english_small is: 0.2686681452718239 seconds.
Number of collisions are: 81165
The probe length is: 296790
Average probe length is: 2.495648444792008 

Time taken to read french is: 1.0103521240034707 seconds.
Number of collisions are: 169313
The probe length is: 934937
Average probe length is: 4.324307948474827

[Quadratic probing]

Time taken to read english_large is: 0.5559985833180413 seconds.
Number of collisions are: 11760
The probe length is: 112724
Average probe length is: 1.1595091393480563 

Time taken to read english_small is: 0.22720943105418212 seconds.
Number of collisions are: 37927
The probe length is: 167262
Average probe length is: 1.4064730960369314 

Time taken to read french is: 0.6657015709613425 seconds.
Number of collisions are: 82352
The probe length is: 370314
Average probe length is: 1.7127911010383663

[Seperate Chaining]

Time taken to read english_large is: 0.5956396251078936 seconds.
Number of collisions are: 11710
The probe length is: 112687
Average probe length is: 1.1591285474762645 

Time taken to read english_small is: 0.23650055391056324 seconds.
Number of collisions are: 37793
The probe length is: 167069
Average probe length is: 1.4048501971864147 

Time taken to read french is: 0.7276685689171218 seconds.
Number of collisions are: 82379
The probe length is: 370287
Average probe length is: 1.7126662195601396 


'''

#As we can see in the results, the hash values of number of collisions, probe length and a
#average lengths have a little difference with quadratic probing but seperate
#chaining have efficient and better results than quadratic probing.
#Overall, the seperate chaining method is taking less time than the other two as we
#we can see as results that seperate chaining has less number of collisions, prob length
# and average prob length too. Moreover, seperate chaining gives the average
#prob length more closer to 1.0 which makes it more stable that's why seperate
#chaining is better way to solve collisions than other ones.












