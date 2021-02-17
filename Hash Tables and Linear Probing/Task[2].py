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

class HashTableLinear:

    # a is the base used for hashing
    def __init__(self, a=108, size=400000):
        """
                    Functionality: initialisation method
                    Precondition: size and a value are defined
                    Post-condition: none
                    Error handling: none
                    Time complexity: O(1)
                    Space complexity: O(1)
                    Return Value: none
                    Parameters: self, a, size
                    Arguments: table_size, count, a, array, collisions, probe_length
                """
        self.table_size = size
        self.count = 0
        self.a = a
        self.array = build_array(self.table_size)
        self.collisions = 0
        self.probe_length = 0

    def __len__(self):
        """
                    Functionality: to find the length of hash table
                    Precondition: none
                    Post-condition: none
                    Error handling: none
                    Time complexity: O(1)
                    Space complexity: O(1)
                    Return Value: self.count
                    Parameters: self
                    Arguments: none
                """
        return self.count

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
        a=108
                       
        h = 0
        for c in key:
            h = (h * a + ord(c)) % self.table_size
        return h
        
    def __str__(self):
        """
                            Functionality: to convert value and key pair to a string
                            Precondition: only key and value are taken as input to convert to string
                            Post-condition: key is first and value is second
                            Error handling:
                            Time complexity: O(N)
                            Space complexity: O(N)
                            Return Value:
                            Parameters:
                            Arguments:
                """
        result = ""
        for i in range(len(self.array)):
            if self.array[i] is not None:
                (key, value) = self.array[i]
                result += "(" + str(key) + ": " + str(value) + "), "
        return result

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
                while(position >= self.table_size):
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

    my_table = HashTableLinear()

#    a=[101,108,151,201,251,301,351,401,451,501]
#    size=[20000,40000,60000,80000,100000,150000,180000,200000,300000,400000]

#    for i in range(len(table)):
#        a=table[i]
#        i+=1

          
    # Reading first file
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



"""
For a=108 and tablesize=400000

Time taken to read english_large is: 0.6237680474302212 seconds.
Number of collisions are: 44558
The probe length is: 186698
Average probe length is: 1.9204254399950627 

Time taken to read english_small is: 0.26552179057995695 seconds.
Number of collisions are: 81165
The probe length is: 296790
Average probe length is: 2.495648444792008 

Time taken to read french is: 1.072480458292775 seconds.
Number of collisions are: 169313
The probe length is: 934937
Average probe length is: 4.324307948474827

For a=101 and tablesize=300000

Time taken to read english_large is: 0.5306637346239557 seconds.
Number of collisions are: 17362
The probe length is: 125937
Average probe length is: 1.2954215826450106 

Time taken to read english_small is: 0.2709540491414184 seconds.
Number of collisions are: 46500
The probe length is: 196228
Average probe length is: 1.6500424644517881 

Time taken to read french is: 0.9037168323366452 seconds.
Number of collisions are: 108493
The probe length is: 721064
Average probe length is: 3.335094008001665

For a=111 and tablesize=300000
Time taken to read english_large is: 0.5862319601213999 seconds.
Number of collisions are: 35134
The probe length is: 146588
Average probe length is: 1.5078432784389562 

Time taken to read english_small is: 0.24131016093259494 seconds.
Number of collisions are: 70137
The probe length is: 226133
Average probe length is: 1.901507698258537 

Time taken to read french is: 0.8161157633291775 seconds.
Number of collisions are: 154605
The probe length is: 640864
Average probe length is: 2.9641497652690734 

For a=121 and tablesize=350000
Time taken to read english_large is: 0.5388436504837946 seconds.
Number of collisions are: 13684
The probe length is: 116223
Average probe length is: 1.1955007868994105 

Time taken to read english_small is: 0.23894348291332468 seconds.
Number of collisions are: 40678
The probe length is: 173859
Average probe length is: 1.4619459650362 

Time taken to read french is: 0.6826106557903188 seconds.
Number of collisions are: 91082
The probe length is: 419082
Average probe length is: 1.9383548021553618 

For a=126 and tablesize=325000
Time taken to read english_large is: 0.5701655088773081 seconds.
Number of collisions are: 27251
The probe length is: 134731
Average probe length is: 1.3858790129298373 

Time taken to read english_small is: 0.2365348933975423 seconds.
Number of collisions are: 59160
The probe length is: 204637
Average probe length is: 1.7207520832807783 

Time taken to read french is: 0.7168270505105273 seconds.
Number of collisions are: 132292
The probe length is: 540853
Average probe length is: 2.5015748941976366

For a=131 and tablesize=375000

Time taken to read english_large is: 0.545398457505896 seconds.
Number of collisions are: 12497
The probe length is: 113963
Average probe length is: 1.172253823919685 

Time taken to read english_small is: 0.23241510656469966 seconds.
Number of collisions are: 39109
The probe length is: 170125
Average probe length is: 1.4305474971199852 

Time taken to read french is: 0.667259720635333 seconds.
Number of collisions are: 86426
The probe length is: 393438
Average probe length is: 1.8197451492796188


For a=129 and tablesize=395000
Time taken to read english_large is: 0.5779225339615275 seconds.
Number of collisions are: 11864
The probe length is: 112800
Average probe length is: 1.1602908956252507 

Time taken to read english_small is: 0.2400520608751272 seconds.
Number of collisions are: 38205
The probe length is: 167845
Average probe length is: 1.4113754277978188 

Time taken to read french is: 0.6682882514146075 seconds.
Number of collisions are: 83457
The probe length is: 375145
Average probe length is: 1.735135635161074

For a=137 and tablesize=275000
Time taken to read english_large is: 0.62736979306293 seconds.
Number of collisions are: 16840
The probe length is: 123126
Average probe length is: 1.2665068866556262 

Time taken to read english_small is: 0.24485942279940098 seconds.
Number of collisions are: 45629
The probe length is: 188970
Average probe length is: 1.5890113771095582 

Time taken to read french is: 0.8219867710703441 seconds.
Number of collisions are: 108783
The probe length is: 646460
Average probe length is: 2.990032607941537 


For a=139 and tablesize=300000
Time taken to read english_large is: 0.5545253466382827 seconds.
Number of collisions are: 15820
The probe length is: 120847
Average probe length is: 1.2430644846066017 

Time taken to read english_small is: 0.2236695742924698 seconds.
Number of collisions are: 43997
The probe length is: 183505
Average probe length is: 1.5430572723526987 

Time taken to read french is: 0.7200648080113637 seconds.
Number of collisions are: 102104
The probe length is: 522621
Average probe length is: 2.4172475197150853 

For a=147 and tablesize=300000
Time taken to read english_large is: 0.5749902395298663 seconds.
Number of collisions are: 35138
The probe length is: 146480
Average probe length is: 1.5067323616239958 

Time taken to read english_small is: 0.24189050300592274 seconds.
Number of collisions are: 70035
The probe length is: 225763
Average probe length is: 1.8983964413948522 

Time taken to read french is: 0.7956946698393544 seconds.
Number of collisions are: 154628
The probe length is: 642056
Average probe length is: 2.9696630512707847

For a=153 and tablesize=350000
Time taken to read english_large is: 0.5786916665596854 seconds.
Number of collisions are: 13542
The probe length is: 115977
Average probe length is: 1.1929703652653343 

Time taken to read english_small is: 0.23678371930926834 seconds.
Number of collisions are: 40525
The probe length is: 173605
Average probe length is: 1.459810129243292 

Time taken to read french is: 0.6566851857585488 seconds.
Number of collisions are: 91148
The probe length is: 419366
Average probe length is: 1.9396683702967092 


For a=129 and tablesize=395000, it's giving the best result among all 10 values
because it's taking less time and giving good amount of collisions and having
balanced prob length average which is really close to 1.
"""

