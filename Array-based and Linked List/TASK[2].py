#Importing the build_array from referential_array
from referential_array import build_array

# Preconditions: The maximum capacity of the array must be at least 20
# otherwise an error will be raised.
# Postconditions: Nothing


# class ddefining named List


class List:
    
    # Asserting max_capacity is positive
# preconditions:  The array takes max capacity and buildarray 
# postconditions: nothing
# complexity: O(1) in all case
    def __init__(self,max_capacity):
        assert max_capacity > 20, 'Max capacity has to be >= 20'
        self.count=0
        self.array=build_array(max_capacity)

#   string format which is as below in the function in the time of printing
# preconditions:  The array takes nothing
# postconditions: The output would be the structure of the printed string
# complexity: O(1) in all case
    def __str__(self):
        string='['
        for i in range(self.count):
            string+=str(self.array[i])
            string+=','
        string+=']'
        return string

 #  Length method for the length of the list
 # preconditions:  The array counts the number of items
# postconditions: The output would be the total of items
# complexity: O(n) in all case
    def __len__(self):
        return self.count

 #  contains method which returns true when the item matches with the
 #  with any other item in the list
  # preconditions:  The array takes the item 
# postconditions: The output would be true if tje item match with any item in the list
# And false if there's no item matched from the list
# complexity: O(n) in all case
    def __contains__(self,item):
        for i in range(self.count):
            if self[i]==item:
                return True
            return False
    # get item method to make sure the index is valid between lengths of an array
# and returns that item
 # preconditions:  The array takes the index 
# postconditions: The output would be that item or will raise error if there's no item so
# complexity: O(n) in all case 
    def __getitem__(self,index):
        valid_index= -len(self.array) <= index <= len(self.array)
        if valid_index:
            for i in range(self.count):
                if index == i:
                    return self.array[i]

                elif index == -i:
                    return self.array[self.count-i+1]

        else:
            raise IndexError

 #  set item method which has same as last but just changing the range
 #  in the negative indexes
 # preconditions:  The array takes the item and item
# postconditions: The output would be- if the current index is equal to index given
# then that item will be equal to that index in the array
# complexity: O(n) in all case

    def __setitem__(self,index,item):
        valid_index= -len(self.array) <= index <= len(self.array)
        if valid_index:
            for i in range(self.count):
                if index == i:
                    self.array[i]=item

            for i in range(-self.count,0,-1):
                if index==i:
                    self.array[self.count-i]=item
        
        else:
            raise IndexError

#   eq method to check whether the item is matching with the items in
#   other arrays and return true when it does match and false otherwise
 # preconditions:  The array inputs the item
# postconditions: The output would be true if both array's item is same
# complexity: O(n) in all case
    def __eq__(self,other):
        matchingOfLength = (self.count == other.count)

        matchingOfItems = False
        for i in range(self.count):
            if self.array[i]==other.array[i]:
                matchingOfItems = True

        if matchingOfItems and matchingOfLength:
            return True
        else:
            raise False

#   This method checks in case the list is full and more than length, if it
#   does then it reset the length to the original length of an array

 # preconditions:  It checks the length of array
# postconditions: The output would be the length of array if it crosses the length
# complexity: O(n) in all case
    def is_full(self):
        return self.count >= len(self.array)

#   This method checks in case the list is empty, if it
#   does then it sets the length to 0
 # preconditions:   It checks the length of array
# postconditions: The output would be the length of array if it's zero
# complexity: O(n) in all case
    def is_empty(self):
        return self.count == 0

 #  In this method, if the array list isn't full then it will keep
 #  appending the items by increasing the counter by 1 each time
# preconditions:   It takes the item
# postconditions: The output would be it will append the item to list
# complexity: O(1) in all case
    def append(self,item):
        if not self.is_full():
            self.array[self.count]=item
            self.count +=1
        else:
            raise Exception

#   In insert method, if both items match with each other, it inserts the item
#   these are getting inserted by both positive and negative values of index
# preconditions:   It takes the index and item in
# postconditions: The output would be the item which will be matched with any other item
# complexity: O(n) in all case
    def insert(self,index,item):
        if j not in range(-len(self), len(self)):
            raise IndexError

        else:
            for i in range(self.count):
                if j==i:
                    self.count +=1

                    for k in range(self.count-1,j,-1):
                        self[k]=self[k-1]
                    self[j] = item

                elif j==-i:
                    
                    self.count+=1
                    for k in range(-1,j-1,-1):
                        self[k]=self[k-1]
                    self[j] = item

                else:
                     
                    raise IndexError

#   Remove method remove the given item in the list if it's in the list
# preconditions:   It takes the item in
# postconditions: It will check whether there is any item match with the one given and
#                  if it does then it will remove that item or else it would just raise the valueerror
# complexity: O(n) in all case
    def remove(self,item):
        for i in range(len(self)):
            if self[i]==item:
                for j in range[i+1,self.count]:
                    self[j-1]=self[j]
                    
                self.item= None
                self.count-=1
                
            else:
                raise ValueError

#   Delete will remove the item in the list if the index of the item is
#   in the list
# preconditions:  It takes the index in
# postconditions: The output would include the item removed from the index given in the input or else it will raise IndexError
# complexity: O(n) in all case
    def delete(self,position):
        if position >= self.count:
            raise IndexError("index is empty")
        if self.array[position] is None:
            raise IndexError("index is empty")
        while position < self.count and position < 50:
            self.array[position] = self.array[position+1]
            position += 1
        self.array[position] = None
        self.count-=1
        

#   sort would sort all items in the in ascending order by using minimum
#   and maximum item according to index in the list
# preconditions:  It takes the reverse in 
# postconditions: The output would be the list in a sorted order 
# complexity: O(n**2) in best case and O(n) is worst case
    def sort(self,reverse):
        if reverse=='False':
            min=self[0]
            for i in range(len(self)):
                if self[i]<min:
                    self[i],min=min,self[i]
            return self

        else:
            max=self[0]
            for i in range(len(self)):
                if self[i]>max:
                    self[i], max=max, self[i]
            return self

#   iterative method which will return the item it gets
#preconditions:  nothing 
# postconditions: it will go through list one by one item 
# complexity: O(n) in all cases
    def __iter__(self):
        return self

#   this method will check if the item is in the list and it will go through
#   the list and print the item as an index increases
#preconditions:  It takes the list in 
# postconditions: The output would be all the items in the list  
# complexity: O(n) is all cases
    def __next__(self,a_list):

        f=a_list
        for item in f:
            print(item)
        
        if self.current is None:
            raise StopIteration
        else:
            item_required=self.current.item
            self.current=self.current.next
            return item_required


# Testing algorithm to print the updated length of list 
def sizeresetting():
    size = 50
    a_list = List(size)
    a_list.append(5)
    a_list.append('And')
    a_list.append(10)
    print(a_list)
    print("The original size of the list is")
    print(len(a_list.array))
 
# If the list is full then increase the size to double and if the size is less than
# decrease it by deviding by 2
    if a_list.is_full():
        a_list.append(5)
        new_array = List(2*size)
        for i in range(len(a_list)):
            new_array.count += 1
            new_array[i] = a_list[i]
        a_list = new_array
    print("The original list")
    print(a_list)
    print("The size of the list after appending an item in a full list is") 
    print(len(a_list.array))


    
    if a_list.count < (1/8)*(len(a_list.array)):
        new_array = List(round(size/2))
        for i in range(len(a_list)):
            if i%2 == 0:
                new_array.count += 1
            new_array[i] = a_list[i]
        a_list = new_array
    print("The size of the list after removing an item in a full list is")
    print(len(a_list.array))

sizeresetting()   

