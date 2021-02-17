"""---------------------------------------------------------------------------------------------------------------------
--------------------------------------------Task1-----------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
"""


def lookup1(data_file):
    """
    Functionality of the function : - Getting the word and id from the file
    Time complexity: O(C_I),
      where C_I is the number of characters in data_file

    Return:
    returns the list having all the word and id
    Parameter:
    the name of the file
    Precondition: filename
    """

    file1 = open(data_file, 'r')
    song_id=[]

    for line1 in file1:
        element = line1.strip('\r\n').split(':')
        element1= element[1].split()

        element0 = element[0]
       # print(element1)


        for i in range(len(element1)):
            song_id.append((element1[i], element0))

            #print(song_id)
    file1.close()
    return song_id


def lookup2(query_file):
    """
    Functionality of the function : - Getting the word from the file
    Time complexity: O(C_I + C_Q + C_P ),
      where C_Q is the number of characters in query_file

    Return:
    returns the list having all the word
    Parameter:
    the name of the file
    Precondition: filename
    """

    file2 = open(query_file, 'r')
    song_lyrics=[]


    for line2 in file2:
        elements= line2.rstrip()
        song_lyrics.append((elements))

    file2.close()
    return song_lyrics






class trie_node:
    """
    Functionality of the function : - Making the trie to get word and id from the file

    """
    # Trie node class
    def __init__(self):
        self.children = [None] * 26
        self.id = []

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = trie_node()

    def insert(self, key, id):
        """
        function: Inserting the words into trie
        """

        Root = self.root
        for level in range(len(key)):
           # print(key[level])
            index = ord(key[level]) - ord('a')

            # if current character is not present
            if not Root.children[index]:
                Root.children[index] = trie_node()
            Root = Root.children[index]

            # mark last node as leaf
        if len(Root.id) == 0:
            Root.id.append(id)
        elif Root.id[-1] != id:

            Root.id.append(id)

        Root.isEndOfWord = True
        return Root.id

    def search(self, key):

        """"
        Functionality: searching for each word in the trie
        """
        Root= self.root
        for level in range(len(key)):
            index = ord(key[level])-ord('a')
            if not Root.children[index]:
                return False
            Root = Root.children[index]

        if Root != None and Root.isEndOfWord:
            return Root.id
        else:
            return None





def lookup():
    """
    Functionality of the function : - Getting the id from the word
    Time complexity:  O(CI + CQ + CP ), where
• CI is the number of characters in data_file
• CQ is the number of characters in query_file
• CP is the number of characters in song_ids.txt

    Return:
    returns the list having all the word and id
    Parameter:
    the name of the file
    Precondition: filename
    """
    # Input keys (use only 'a' through 'z' and lower case)
    keys1 = lookup1('example_songs.txt')
    keys2 = lookup2('example_queries.txt')

    t = Trie()

    for i in range(len(keys1)):
        t.insert(keys1[i][0], keys1[i][1])


    for key in keys2:
        result = t.search(key)

        if result:
            if result is not None:

                print(result)
            else:
                print("Not found")
        else:
            print("Not found")


if __name__ == '__main__':
    lookup()






"""---------------------------------------------------------------------------------------------------------------------
    --------------------------------------------Task2-----------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------"""

class Node(object):
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False
        # Count of words (leaf nodes) starting from this node. It will help to find out the number of words/count starting with some prefix.
        self.wordsNum = 0
        self.id= []


class Trie2(object):
    def __init__(self):
        self.root = Node()



    # Time complexity: O(length_of_word)
    def insert(self, word ,id):
        cur = self.root
        child = cur
        for ch in word:
            if child.children[ord(ch) - 97] is None:
                value = Node()
                child.children[ord(ch) -97] = value
            if len(child.id) == 0:
                child.id.append(id)
            else:
                if child.id[-1] != id:
                    child.id.append(id)

            child.wordsNum+=1
            child = child.children[ord(ch) -97]
            if len(child.id) == 0:
                child.id.append(id)
            else:
                if child.id[-1] != id:
                    child.id.append(id)

        child.endOfWord = True









    def prefix_search(self, prefix):

        cur = self.root
        for ch in prefix:
            child = cur.children[ord(ch)-97]
            if cur.children[ord(ch)-97] is None:
                return False
            cur = child
        id_length = len(cur.id)
        stop = False
        while not stop:
            for i in range(26):
                stop = True
                if cur.children[i] is not None:
                    stop = False
                    if len(cur.children[i].id) == id_length:
                        cur = cur.children[i]
                        prefix = prefix + chr(i+97)
                        break

        return prefix















def most_common(data_file, query_file):
    """
    Functionality of the function : - Getting the word appeared most from the prefix
    Time complexity:  O(CI + CQ + CP ), where
• CI is the number of characters in data_file
• CQ is the number of characters in query_file
• CP is the number of characters in song_ids.txt

    Return:
    returns the list having all the word and id
    Parameter:
    the name of the file
    Precondition: filename
    """
    # Input keys (use only 'a' through 'z' and lower case)

    id = []
    word = []
    word_pre_t = Trie2()

    keys1 = lookup1(data_file)
    keys2 = lookup2(query_file)

    for i in range(len(keys1)):
        id.append(keys1[i][1])
        word.append(keys1[i][0])

        word_pre_t.insert(keys1[i][0], keys1[i][1])



    for i in keys2:

        result = word_pre_t.prefix_search(i)

        if result:
            if result is not None:

                print(result)
            else:
                print("Not found")
        else:
            print("Not found")





most_common('example_songs.txt','teea.txt')




"""
------------------------------------------------------------------------------------------------------------------------
--------------------------------------------Task3-----------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
"""



def palindromic_substrings(string):
    palindrome_subs = []

    for x in range(2,len(string)+1):
        start, end = 0, x

        while len(string)+1 > end:

            substring = string[start:end]

            if(len(substring)%2==0):
                mid = len(substring)//2
                if( substring[0:mid] == substring[mid:][::-1] ):
                    palindrome_subs.append((substring,(start,end-1)))
            else:
                midPoint = len(substring)//2
                if(substring[0:midPoint] == substring[(mid+1):][::-1]):
                    palindrome_subs.append((substring,(start, end-1)))

            start = start+1
            end = end + 1

    return palindrome_subs

print(palindromic_substrings("ababcbaxx"))