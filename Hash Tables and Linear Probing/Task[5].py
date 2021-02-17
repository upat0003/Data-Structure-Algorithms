# The Mind and its Education

from referential_array import build_array


class HashTableLinear:
    # a is the base used for hashing
    def __init__(self, a=33, size=399989):
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
        a = 133
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
                position = (position + s * s) % self.table_size
                if position >= self.table_size:
                    position = 0
                s += 1

        #self.__setitem__(key, value)

        # doubling the size of the underlying array (and rehashing) every time the load exceeds 2/3
        if self.count > int((2 / 3) * self.table_size):
            self.array2 = build_array(2*self.table_size)

            # Rehash for all keys in the array
            for item in self.array:
                position = self._hash_value(item[0])
                self.array2[position] = self.array[position]



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
                # Find next position using quadratic probing if current position is already being used
                s = 1
                position = (position + s * s) % self.table_size
                if position >= self.table_size:
                    position = 0
                s += 1

        h = self._hash_value(key)
        self.__setitem__(key, value)

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
        position = self._hash_value(key)
        if self.array[position] is None:
            return False

        elif self.array[position][0] == key:
            return True



if __name__ == "__main__":

    my_table = HashTableLinear()
    my_table2 = HashTableLinear()

    # Reading file
    file = open('textfile3.txt')
    maximum = None
    common = []

    for line in file:
        word = line.split(' ')
        #print(word)

        if word is None:
            continue

        for i in range(len(word)):
            if word[i] not in my_table:
                value = 1
                my_table[word[i]] = value

            else:
                my_table[word[i]] += 1

            #print("Max:", maximum)

            #print(my_table[word[i]])
            if maximum is None:
                maximum = word[i]
            else:
                #print("Table Max:", my_table[maximum])
                #print("Table Word:", my_table[word[i]])
                if my_table[word[i]] is not None and my_table[maximum] < int(my_table[word[i]]):
                    maximum = word[i]

    for line in file:
        word = line.split(' ')
        commonWords = 0
        uncommonWords = 0
        rareWords = 0
        misspelledWords = 0
        totalWords = commonWords + uncommonWords + rareWords + misspelledWords

        for i in range(len(word)):

            if my_table[word[i]] > int(my_table[maximum]/100):
                my_table2[word[i]] = 'common'
            if my_table[word[i]] < int(my_table[maximum]/100) and my_table[word[i]] > int(my_table[maximum]/1000):
                my_table2[word[i]] = 'uncommon'
            if my_table[word[i]] < int(my_table[maximum]/1000):
                my_table2[word[i]] = 'rare'

            if my_table2[word[i]] == 'common':
                commonWords += my_table[word[i]]
            elif my_table2[word[i]] == 'uncommon':
                uncommonWords += my_table[word[i]]
            elif my_table2[word[i]] == 'rare':
                rareWords += my_table[word[i]]
            else:
                misspelledWords += 1

    #print(my_table)
    print("Most common word:", maximum)
    print("Times occured:", my_table[maximum])
    print(my_table2)

   # print('Percentage of common words:', commonWords/totalWords*100)
   # print('Percentage of uncommon words:', uncommonWords / totalWords * 100)
   # print('Percentage of rare words:', rareWords / totalWords * 100)
   # print('Percentage of misspelled words:', misspelledWords / totalWords * 100)
