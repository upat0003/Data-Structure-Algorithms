import sys
import heapq
import math

class Graph:

    def __init__(self, vertices_filename, edges_filename):
        """"
        Time complexity: O(V + E),
        Where, V is the number of lines in vertices_filename
               E is the number of ines in edges_filename

        Functionality of the function: Builds an adjacency list in order to represent the graph
        Return: It doesn't return anything but the job is to create a graph which is done as in the task
        Parameter: name of the files
        Precondition: the file should be containing the required data of vertex and edge being required to build the graph
        """

        self.vertices = []
        self.vertices2= []
        self.graph = [[]]
        self.edges = []
        self.words = []
        self.temp = []
        self.n_vert = 0
        self.minDistance = sys.maxsize

        f = open(vertices_filename)
        lines = f.readlines()
        for line in lines:
            self.vertices.append(line.rstrip())
        f.close()
        for i in self.vertices:
            self.temp.append(i.split())
        self.n_vert = int(self.temp[0][0])
        self.temp = self.temp[1:]
        for i in self.temp:
            self.words.append(i[1])
            self.vertices2.append(i[1])

        f = open(edges_filename)
        lines = f.readlines()
        for line in lines:
            x = line.rstrip().split()
            self.edges.append((int(x[0]), int(x[1])))

        self.adj_list = [[]for i in range(self.n_vert)]
        self.words_comb = ['' for i in range(self.n_vert)]
        self.words_comb[0] = self.words[0]

        for i in self.edges:
            self.adj_list[i[0]].append(i[1])
            self.adj_list[i[1]].append(i[0])



    def solve_ladder(self, start_vertex, target_vertex):
        """
        Time complexity: O(V + E),
        Where, V is the number of lines in vertices_filename
               E is the number of ines in edges_filename

        Functionality of the function: Builds a path between start and target vertex in sequence in the graph
        Return: It returns the list of words between two vertices
        Parameter: name of the files
        Precondition: the file should be containing the required data of vertex and edge being required to build the graph
        """

        visited = [False]*(len(self.adj_list))

        travelled=[]
        queue = [start_vertex]

        visited[start_vertex] = True

        while len(queue) != 0:
            node = queue.pop(0)


            if node not in travelled:
                travelled.append(node)
                neighbours = self.adj_list[node]

                for neighbour in neighbours:
                    queue.append(neighbour)
                    if self.words_comb[neighbour] is '':
                        self.words_comb[neighbour] = self.words_comb[node] + ' ' +self.words[neighbour]




        target = self.words_comb[target_vertex]
        if start_vertex !=0:
            target = [self.words[start_vertex]] + target.split()
            return target
        else:
            target = target.split()
            return target




    def weight(self, char1, char2):
        """
        Time complexity: O(n) where n is the length of character
        Functionality of the function: It counts the value for the difference between two characters and using ord()
                                       function to return the weight of the edge
        Return: It returns the weight of an edge
        Parameter: two words
        """
        for i in range(len(char1)):
            if char1[i] != char2[i]:
                value= math.pow(ord(char1[i])- ord(char2[i]), 2)

                return int(value)






    def Djikstra(self, start_vertex):
        """
        Time complexity: Time complexity: O(E×log(V)) time,
                                            Where, V is the number of vertices in the graph
                                                   E is the number of edges in the graph
        Functionality of the function: It goes through the edges in the graph and keep finding the cheapest distance and
                                       update it over
        Return: Returns the shortest path path
        Parameter: start_vertex to start travelling from a vertex
        """

        q = []
        distance = [math.inf] * (len(self.vertices)-1)
        distance[start_vertex] = 0
        pre = [math.inf]*(len(self.vertices)-1)
        heapq.heappush(q, start_vertex)

        # While the heap "q" has items in it
        while q:
            actualVertex = heapq.heappop(q)

            for edge in range(len(self.adj_list[actualVertex])):

                weight =  self.weight(self.vertices2[actualVertex], self.vertices2[self.adj_list[actualVertex][edge]])

                v = self.adj_list[actualVertex][edge]

                newDistance = distance[actualVertex] + weight

                if newDistance < distance[v]:

                    distance[v] = newDistance
                    pre[v]= actualVertex
                    heapq.heappush(q, v)
        return [pre, distance]


    def check_word(self,name,char):
        """
        Time complexity: O(n) where n is the length of character
        Functionality of the function: It checks if the given required character is present in the word
        Return: It returns the true value
        Parameter: one word and char
        """
        for i in range(len(name)):

            if name[i] == char:
                return True
            return True



    def cheapest_ladder(self, start_vertex, target_vertex, req_char):
        """
         Time complexity: Time complexity: O(E×log(V)) time,
                                            Where, V is the number of vertices in the graph
                                                   E is the number of edges in the graph
        Functionality of the function: It goes through the edges in the graph and keep finding the cheapest distance
                                       using Dijkstra which also puts the values of the cheapest distance into the new
                                       array and checks if the word contains in the cheapest path
        Return: It returns the cheapest weight with the path
        Parameter: starting and target vertex with the character we would like to check for
        """

        value = self.Djikstra(start_vertex)
        gmail = []
        reqcharFound = False

        vertex = value[0][target_vertex]
        gmail.append(self.vertices2[vertex])
        while start_vertex != vertex:
            vertex = value[0][vertex]
            gmail.append(self.vertices2[vertex])


        if(self.check_word(value,req_char) and not reqcharFound):
            gmail.reverse()
            tuple_array = (value[1][target_vertex], gmail)
        return tuple_array

