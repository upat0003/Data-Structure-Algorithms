from referential_array import build_array

# Preconditions: The max_capacity of the array has to be at least 0
# otherwise an error is raised.
# The file should contain only simple text to be able to be operated
# upon.
# Postconditions: The Editor is a list containing lines of text as its elements.

# Defining class
class List:

    # Asserting max_capacity is positive
    # Asserting max_capacity is positive
# preconditions:  The array takes max capacity and buildarray 
# postconditions: nothing
# complexity: O(1) in all case
    def __init__(self, max_capacity):
        assert max_capacity > 0, 'Max capacity has to be positive'
        self.count = 0
        self.array = build_array(max_capacity)


#   string format which is as below in the function in the time of printing
# preconditions:  The array takes nothing
# postconditions: The output would be the structure of the printed string
# complexity: O(1) in all case
    def __str__(self):
        ans = '['
        for i in range(self.count):
            ans += str(self.array[i])
            ans += ', '
        ans += ']'
        return ans

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
    def __contains__(self, item):
        for i in range(self.count):
            if self[i] == item:
                return True
            return False

  # get item method to make sure the index is valid between lengths of an array
# and returns that item
 # preconditions:  The array takes the index 
# postconditions: The output would be that item or will raise error if there's no item so
# complexity: O(n) in all case 
    def __getitem__(self, index):

        # Defining valid indices
        valid_index = -len(self.array) <= index < len(self.array)
        if valid_index:
            for i in range(self.count):
                if index == i:
                    return self.array[i]

                elif index == -i:
                    return self.array[self.count - i + 1]

        else:
            raise IndexError

    # Setitem method
     #  set item method which has same as last but just changing the range
 #  in the negative indexes
 # preconditions:  The array takes the item and item
# postconditions: The output would be- if the current index is equal to index given
# then that item will be equal to that index in the array
# complexity: O(n) in all case
    def __setitem__(self, index, item):

        # Defining valid indices
        valid_index = -len(self.array) <= index < len(self.array)
        if valid_index:
            for i in range(self.count):
                if index == i:
                    self.array[i] = item
            for i in range(-self.count, 0, -1):
                if index == i:
                    self.array[self.count - i] = item

    # Equal method
#   eq method to check whether the item is matching with the items in
#   other arrays and return true when it does match and false otherwise
 # preconditions:  The array inputs the item
# postconditions: The output would be true if both array's item is same
# complexity: O(n) in all case
    def __eq__(self, other):

        length_match = (self.count == other.count)
        items_match = False
        for i in range(self.count):
            if self.array[i] == other.array[i]:
                items_match = True

        if length_match and items_match:
            return True
        else:
            return False

#   This method checks in case the list is empty, if it
#   does then it sets the length to 0
 # preconditions:   It checks the length of array
# postconditions: The output would be the length of array if it's zero
# complexity: O(n) in all case
    # Empty and full methods
    def is_empty(self):
        return self.count == 0

#   This method checks in case the list is full and more than length, if it
#   does then it reset the length to the original length of an array

 # preconditions:  It checks the length of array
# postconditions: The output would be the length of array if it crosses the length
# complexity: O(n) in all case
    def is_full(self):
        return self.count >= len(self.array)

#  In this method, if the array list isn't full then it will keep
 #  appending the items by increasing the counter by 1 each time
# preconditions:   It takes the item
# postconditions: The output would be it will append the item to list
# complexity: O(1) in all case

    # Method to append item to list
    def append(self, item):
        if not self.is_full():
            self.array[self.count] = item
            self.count += 1
        else:
            raise Exception


#   In insert method, if both items match with each other, it inserts the item
#   these are getting inserted by both positive and negative values of index
# preconditions:   It takes the index and item in
# postconditions: The output would be the item which will be matched with any other item
# complexity: O(n) in all case
    # Method to insert item into list at specified position
    def insert(self, index, item):

        if index not in range(-len(self), len(self)):
            raise IndexError
        else:
            for i in range(self.count):
                if index == i:
                    self.count += 1
                    for j in range(self.count - 1, index, -1):
                        self[j] = self[j - 1]
                    self[index] = item

                elif index == -i:
                    self.count += 1
                    for j in range(-1, index - 1, -1):
                        self[j] = self[j - 1]
                    self[index] = item

#   Remove method remove the given item in the list if it's in the list
# preconditions:   It takes the item in
# postconditions: It will check whether there is any item match with the one given and
#                  if it does then it will remove that item or else it would just raise the valueerror
# complexity: O(n) in all case
    # Method to remove a specific item from list
    def remove(self, item):
        for i in range(len(self)):
            if self[i] == item:
                for j in range(i + 1, self.count):
                    self[j - 1] = self[j]
                self.count -= 1


    # Method to delete an item at a specific index from the list
#   Delete will remove the item in the list if the index of the item is
#   in the list
# preconditions:  It takes the index in
# postconditions: The output would include the item removed from the index given in the input or else it will raise IndexError
# complexity: O(n) in all case
    def delete(self, index):
        if index not in range(-len(self), len(self)):
            raise IndexError
        else:
            for i in range(len(self)):
                if i == index:
                    self.remove(self[i])
        return self

# Defining editor class
class Editor():

    # print menu
    def print_menu(self):

        print('\n')
        print('The list supports the following operations:')
        print('\n')
        print('Insert num: insert a line of text in the list before position num, and raises an exception if no num is given')
        print('Read filename: opens the file, filename, reads all the lines in from the file, put each line as a separate item into a list, and then closes the file.')
        print('Write filename: creates or opens a file, filename, writes every item in the list into the file, and then closes the file.')
        print('Print num1 num2: prints the lines between positions num1 and num2, if num1 < num2.')
        print('Delete num: deletes the line of text in the list at position num, and deletes all the lines if no num is given.')
        print('Search word: takes a word and prints the line numbers in which the target word appears. Search should be case insensitive.')
        print('Quit: quits the program.')


    
    # Method to insert line of text in the list before position num
    #   In insert method, the node would be put in between others and will have the arrow set
#   these are getting inserted by both positive and negative(it's automatically set to 0) values of index
# preconditions:   It takes the index and item in
# postconditions: The output would be node will be inserted according to it's index
# complexity: O(n) in all case
    def insert_num(self, item, num):

        # Raise exception if num is undefined
        if num == None:
            raise AssertionError

        if num not in range(-len(self), len(self)):
            raise IndexError

        else:
            for i in range(self.count):
                if num == i:
                    self.count += 1
                    for j in range(self.count - 1, num, -1):
                        self[j] = self[self.count - j - 1]
                    self[num] = item

                elif num == -i:
                    self.count += 1
                    for j in range(-1, num - 1, -1):
                        self[j] = self[self.count - j - 1]
                    self[num] = item

    # Reading from a file
    # Preconditions: The input condition of the array has to be given as a text file
# Postconditions: It will print the each line contained as an element in the list
#complexity: O(n) for all case
    def read_filename(self, filename):
        file = open(filename)

        # Appending to list
        for line in file:
            a = file.readline()
            List.append(a)
        # Closing file
        file.close()

    # Writing to a file
    # Preconditions: The input condition of the array has to be given as a text file
# Postconditions: It will print the each line contained as an element in the list
# it will p=let you add any lines in a file if we want too
#complexity: O(n) for all case
    def write_filename(self, filename):
        file = open(filename, 'w')

        # writing to file
        for item in List:
            file.write(item)

        # Closing file
        file.close()

 # Print between num1 and num2
        # Preconditions: The input condition of the file will be filename and 2 numbers where number1 is less than number2
# Postconditions: It will print the each line contained as an element in the list according to the condition above
# it will p=let you add any lines in a file if we want too
#complexity: O(n) for all case
    def printn1n2(self, filename, num1, num2):
        assert num1<num2, 'num1 should be less than num2'

        file = open(filename)
        i = 1

        # Appending to list
        for line in file:
            if i > num1 and i < num2:
                a = file.readline()
                print(a)
            i += 1
        # Closing file
        file.close()


    # Delete num
    #   Delete will remove the node in the list if the index of the item is
#   in the list
# preconditions:  It takes the index in
# postconditions: The output would include the item removed from the index given in the input or else it will raise IndexError
# complexity: O(n) in all case
    def delete_num(self, num):

        if num == None:
            for item in List:
                List.remove(item)

        else:
            List.delete(num)

   # Search word
      # Preconditions: The input condition of the file will be filename and a word
# Postconditions: It will print the each line contains the word and as an element in the list 
#complexity: O(n) for all case
    def search_word(self, filename, word):
        file = open(filename)
        i = 1

        for line in file:
            if word in line:
                print(i)
                i += 1

    # Quit
    def quit(self):
        print('Goodbye!')

# Run the file which will print out the menu and the line by line printing
# preconditions:  It takes the file name as an input
# postconditions: The output would be the printing of menu and the lines of all prints
# complexity: O(n) in all case
def RunFile():
    size = 50
    a_list = List(size)
    a_list.append(5)
    a_list.append('Hello')
    a_list.append(10)
    print(a_list)

    print(len(a_list.array))

    # If list becomes full
    if a_list.is_full():
        new_array = List(2*size)
        for i in range(len(a_list)):
            new_array.count += 2
            new_array[i] = a_list[i]
        a_list = new_array
    print(a_list)

    # If contents occupy less than 1/8 space
    if a_list.count < (1/8)*(len(a_list.array)):
        new_array = List(round(size/2))
        for i in range(len(a_list)):
            if i%2 == 0:
                new_array.count += 1
            new_array[i] = a_list[i]
        a_list = new_array
    print(len(a_list.array))

    a_editor = Editor()
    a_editor.print_menu()
    print('\n')
    a_editor.printn1n2('test2.txt', 2, 6)

RunFile()
