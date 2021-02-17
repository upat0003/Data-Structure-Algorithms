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

"""
                    Functionality: 
                    Precondition: 
                    Post-condition: 
                    Error handling: 
                    Time complexity: O(1)
                    Space complexity: O(1)
                    Return Value: 
                    Parameters:
                    Arguments:
"""


class HashTableLinear:

    # a is the base used for hashing para
    def __init__(self, a=33, size=79):
        """
            Functionality: initialisation method
            Precondition: size and a values are defined
            Post-condition: none
            Error handling: none
            Time complexity: O(1)
            Space complexity: O(1)
            Return Value: none
            Parameters: self, a, size
            Arguments: table_size, count, a, array
        """
        self.table_size = size
        self.count = 0
        self.a = a
        self.array = build_array(self.table_size)

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

        a = 101
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
                    Error handling: raises index error if there is not enough space in the table for storage and goes
                    to index 0 if end of list is reached
                    Time complexity: O(N)
                    Space complexity: O(1)
                    Return Value: none
                    Parameters: key, value
                    Arguments: position, array[position], count
        """

        position = self._hash_value(key)
        for _ in range(self.table_size):

            # If there is nothing
            if self.array[position] is None:
                self.array[position] = (key, value)
                self.count += 1
                return

            # Found key
            elif self.array[position][0] == key:
                self.array[position] = (key, value)
                return

            # Try next position
            else:
                position += 1
                if position >= self.table_size:
                    position = 0
        raise IndexError("Not enough space")

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
                raise KeyError("Not found")

            elif self.array[position][0] == key:
                return self.array[position][1]

            else:
                position += 1
                if position >= self.table_size:
                    position = 0

        raise KeyError("Not found")

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

        for item in range(self.count):
            if key in self:
                return True
            else:
                return False


if __name__ == "__main__":
    my_table = HashTableLinear()
    my_table["University"] = "Monash University"
    my_table["currentUnit"] = "FIT1008"
    my_table["Name"] = "Utkarsh"
    my_table["Student ID"] = "29143926"
    my_table["Day"] = "Monday"
    print(my_table)
