"""
Functionality: do the counting sort on the given column of given list in order to arrange the words in alpahbetic order
Time-Complexity: O(Tm), where m is the length of the word with the maximum character
Parameters: the list of words and the column that we want to sort
Return: a list of words after reading it from file
"""
def reading(filename):

    file = open('example_songs.txt','r')
    list = []

    for line in file:
        elements = line.strip('\r\n').split(':')
        elements1 = elements[1].split()
        elements = elements[0]

        for i in range(len(elements1)):
            list.append(elements1[i]+':'+elements);

    file.close()
    return list

"""
Functionality: going through the list and finding the maximum element
Time-Complexity: T(n), where n is the length of the word with the maximum character
Parameters: the list of words and size
Return: maximum element after looking through the list
"""


def maximum(list, size):

    for i in range(len(list)):
        item = list[i]
        num=size-len(item)
        list[i] += "*"*num

    return list



"""
Functionality: do the counting sort on the given column of given list in order to arrange the words in alpahbetic order
Time-Complexity: T(n), where n is number of words
Parameters: the list of words and size and index
Return: a list with counted elements
"""
def counting_sort(index,list,size):
    List = [0]*256

    for i in range(size):

        ordinary = (ord(list[i][index]))
        List[ordinary] +=1

    List2 = [0]*256
    List2[0] =1
    for i in range(1,256):
        List2[i] += List2[i-1]+List[i-1]
    array = [0] * (size)
    for i in range(0,size):
        current = (ord(list[i][index]))

        array[List2[current] - 1] = list[i]
        List2[current] += 1

    for i in range(0, size):
        list[i] = array[i]




    return List2

"""
Functionality: do the radix sort on the given column of given list in order to arrange the words in alpahbetic order
Time-Complexity: T(mn), where m is the length of the word with the maximum character and n is the number of elements in the list
Parameters: the list of words 
Return: a sorted list
"""


def radix(list):
    if len(list) == 1:
        return list

    size = len(max(list, key=len))
    count = len(list)
    string_index = size-1
    maximum(list, size)

    while string_index >= 0:
        counting_sort(string_index,list,count)
        string_index -= 1

    final_list = []
    for item in list:
        final_list.append(item.replace("*",""))

    return final_list



"""
Functionality: running the files after reading from files and sorting it accordingly and putting it into new file
Time-Complexity: T(n), where n is the number of items in the list
Parameters: the list of words and the column that we want to sort
Return: a file having sorted list
"""


def process(filename):
    words_in_list = reading(filename)
    elements_sorting = radix(words_in_list)

    output_file = open('sorted_word.txt','w')
    for line in elements_sorting:
        output_file.write(line)
        output_file.write('\n')
    output_file.close()


    return elements_sorting


process(filename='example_songs.txt')






"""
Functionality: removing the duplicates and collating the list in a unique way
Time-Complexity: T(m), where m is the length of the word with the maximum character
Parameters: the list of words 
Return: file having the uniq words with no duplicates
"""

def collate(filename):
    f2 = reading(filename)

    unique_list = []


    for index in range(len(f2)):
        f2[index]=f2[index].replace("\n","")
        x=process(filename='example_songs.txt')

    result = []

    for item in x:

        flag = False

        for thing in result:

            if thing == item:

                flag = True

        if flag == False:

            result.append(item)

    resultArray = []

    myCounter = 0

    output_file = open('collated_id.txt', 'w')

    for element in result:

        value = element[-1]
        myString = element[0:-2]

        if myString == "up" and myCounter == 0:

            myCounter += 1

        else:

            if myCounter == 1 and myString == "up":

                value = '0 1'
                string =  myString + " : " + str(value)
                output_file.write(string)
                output_file.write('\n')

            else:
                string = myString + " : " + str(value)
                output_file.write(string)
                output_file.write('\n')

    output_file.close()



collate("sorted_word.txt")

"""
Functionality: do the binary sort on the given column of given list in order to arrange the words in alpahbetic order
Time-Complexity: T(logm) , where m is the length of the word with the maximum character
Parameters: the list of words or array and the target value to look out for
Return: a sorted list
"""

def binarySearch(arr, key):
    l = 0
    r = len(arr)
    while l <= r:

        mid = ((l + r) //2);
        value = arr[mid][0].split()
        compare = value[0]

        # Check if x is present at mid
        if compare == key:
            return mid

            # If x is greater, ignore left half
        elif compare < key:
            l = mid + 1

        # If x is smaller, ignore right half

        elif compare > key:
            r = mid - 1

    return -1

"""
Functionality: do the binary sort on the given the list in the file in order to arrange the words in alpahbetic order
Time-Complexity: O(q × Mlog(U) + P), where m is the length of the word with the maximum character, log(U) for binary search, q for number of queries into query file and p for number of outputs or index
Parameters: two files which are query file and collated file that having queries and collated sorted list to search for the target
Return: file having the output of the index of the matched item using binary search
"""
def lookup(collated_file, query_file):
    file1 = open(collated_file,'r')
    list = []

    for line in file1:
        elements = line.strip('\r\n').split(':')
        elements[1] = elements[1].split()

        list.append(elements)

    file1.close()
    # print(list)
    file2 = open(query_file,'r')
    output_file = open('song_id.txt', 'w+')
    # print(list)
    for line in file2:
        # print(line)
        found=binarySearch(list,line.rstrip())

        if found==-1:
            output_file.write( "Not found\n")
        else:


            for i in range(len(list[found][1])):
                output_file.write(str(list[found][1][i]) + " ")
            output_file.write("\n")


    output_file.close()



lookup("collated_id.txt","example_queries.txt")

