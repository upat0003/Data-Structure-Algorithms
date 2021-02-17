"""
------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------Task-1---------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

Functionality of function: To get the maximum total value of coins player can get from two piles
Time complexity: O(NM), where N is the number of elements in pile and M is the number of elements in pile2
Space complexity: O(MN), as above
Input: Inputs are two piles in array format
Return: The maximum value that can be achieved for any player
"""


def best_score(pile1,pile2):
    pile1=[2,3,4]
    pile2=[4,5,6]

    table = [[0 for i in range(len(pile1))]
             for j in range(len(pile2))]

    for i in range(0,len(pile1)):
        for j in range(0,len(pile2)):

            x = 0
            if (i + 2) <= j:
                x = table[i + 2][j]

            y = 0
            if (i + 1) <= (j - 1):
                y = table[i + 1][j - 1]

            z = 0
            if i <= (j - 2):
                z = table[i][j - 2]
            table[i][j] = max(pile1[i] + min(x, y),
                              pile2[j] + min(y, z),
                              pile1[i] + min(y,z),
                              pile2[j] + min(x,y))

    return table[0][len(pile1) - 1]

            # print(pile1)
            # print(pile2)


print(best_score([2,3,4],[4,5,6]))





"""
------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------Task-2-----------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

Functionality of the function: To go through all the elements of table (grid) and use backtracking and recursion
algorithm to return the positions of the visited elements while finding the word
Time Complexity: is_in must run in O(K*N^2), where K is the number of characters in word and N is the length of grid
Space Complexity: O(KN^2) as above
Input: The table (grid) and word 
Return :- The function returns the positions of the word being matched with the grid table
"""


def is_in(grid, word):
    found = False
    row = len(grid)
    column = len(grid[0])
    travelled = set()
    position = [(-1, -1), (0, -1), (1, -1),
                (-1, 0), (0, 0), (1, 0),
                (-1, 1), (0, 1), (1, 1)]

    """
    Functionality of the function: To go through all the elements of table (grid) and use backtracking and recursion
    algorithm to return the positions of the visited elements while finding the word
    Time Complexity: is_in must run in O(K*N^2), where K is the number of characters in word and N is the length of grid
    Space Complexity: O(KN^2) as above
    Input: row(i), column(j) (grid) and word strings being matched
    Return :- The function returns the positions of the word being matched with the grid table
    """
    def recursion(i, j, matchedword):

        print((i, j),matchedword)

        if grid[i][j] != matchedword[0]:
            return False

        travelled.add((i, j))
        if grid[i][j] == matchedword:
            return True

        up = recursion(i-1, j, matchedword[1:]) \
            if i-1 >= 0 and (i-1, j) not in travelled else False

        down = recursion(i+1, j, matchedword[1:]) \
            if i+1 < row and (i+1, j) not in travelled else False

        left = recursion(i, j-1, matchedword[1:]) \
            if j-1 >= 0 and (i, j-1) not in travelled else False

        right = recursion(i, j+1, matchedword[1:]) \
            if j+1 < column and (i, j+1) not in travelled else False

        if up or down or left or right:
            return True
        else:
            travelled.remove((i,j))
            return False

    for i in range(row):
        for j in range(column):
            if grid[i][j] == word[0]:
                found = recursion(i,j,word)
                travelled.clear()
                if found:
                    return True

    return found


grid = [['a', 'b', 'c', 'd'],
        ['e', 'a', 'p', 'f'],
        ['e', 'p', 'g', 'h'],
        ['l', 'i', 'j', 'k']]

word = input('Enter any word you like:  ')
is_in(grid, word)