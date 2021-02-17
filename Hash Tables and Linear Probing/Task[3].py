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
        a = 113
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

        string = ""
        for index in range(self.table_size):
            if self.array[index] is None:
                pass
            else:
                string += str((index,str(self.array[index])))
                string += ","
        return string

    def __setitem__(self, key, value):
        """
                            Functionality: to set a certain value as an item in the hash table
                            Precondition: none
                            Post-condition: none
                            Error handling: raises index error if there is not enough space in the table for storage,
                            goes to index 0 if end of list is reached and double size of array and rehash if it is 2/3
                            filled
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

            # Find next position using quadratic probing if current position is already being used
            else:
                s = 1
                position = (position + s*s) % self.table_size
                while(position >= self.table_size):
                    position = 0
                    s += 1

        self.rehash(key)
        self.__setitem__(key, value)

        # doubling the size of the underlying array (and rehashing) every time the load exceeds 2/3
        if self.count > int(2 / 3) * self.table_size:
            self.table_size *= 2

            # Rehash for all keys in the array
            for key in self:
                self.rehash(key)

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

    print(HashTableLinear(33,400000))

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


'''
#As we can see from the output of both methods, quadratic probing looks more effective
#as it takes less time in this method and it's having less collisions and
#the probe length is smaller too so quadratic probing is really very effective
# and it works fast too.





