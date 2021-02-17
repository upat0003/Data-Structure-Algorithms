
# NAME- UTKARSH PATEL
# STUDENT ID- 29143926
# TASK-1 TO TAASK-5








Location=['land','freshwater','seawater']
Climate=['cold', 'tropical', 'arid', 'temperate','polar']
PlantLife=['conifers', 'mosses','greenalgae', 'flowering', 'ferns']

import random



def getAnimalList(Location, Climate, PlantLife):
#this fuction reads the content of file into list of lists
#it ask for file name and will open file, it will split the length of content in file and append to table
#table- indicates name of animal in raw and all location-climate-plantlife in column which gets printed

    fileToReadAnimalList=input('Enter the name to read the file from: ')
    f=open(fileToReadAnimalList, 'r')

    table=[]

    for length in f:
        length=length.split()
        
        table.append(length)


    
    for index in range(len(table)):
        print("Animals: " + table[index][0])

        plantlife=[]
        climate=[]
        location=[]
        
        
        
        for j in range(len(table[index])):

            if table[index][j] in PlantLife:
                plantlife.append(table[index][j])

           
            if table[index][j] in Climate:
                climate.append(table[index][j])
            
            if table[index][j] in Location:
                location.append(table[index][j])
            
                    
            
        print("Location: " + str(location))
        print("Climate: " + str(climate))
        print("PlantLife: " + str(plantlife))


    f.close()


    return table









def writeAnimalList(number):
#this function is used to write into new file after reading it
#it would take list using parameter with the index on side and write into new file

    newfiletowritein=input('Enter the name to write into new file : ')
    newf=open(newfiletowritein, 'w')

   
    for i in range(len(number)):
        for j in range(len(number[i])):
        
            newf.write(number[i][j] + ' ')
        newf.write('\n')
    
        

    newf.close()



def readGraphFromFile():
#it will display the table corresponding to the graph file
#After opening that file of graph,it would split each line and append to table. it would use the index in range of 1 and length of table. It would find column afterwards
#and convert that table into integer so that table can be read as numbers in file. 
    
    graphFileToReadFrom=input("Enter the filename for new graph to read the file: ")
    graphfile=open(graphFileToReadFrom,'r')

    tableForGraph=[]

    for line in  graphfile:
        line=line.split()
        tableForGraph.append(line)

    for i in range(1,len(tableForGraph)):
        for j in range(len(tableForGraph[i])):

            tableForGraph[i][j]=int(tableForGraph[i][j])
                       
    for i in range(len(tableForGraph)):
        for j in range(len(tableForGraph[i])):

            print(tableForGraph[i][j],end=' ')
        print()
    return tableForGraph


def writeGraph(num):
#it will write that graph file including table to new file
#function would take input as file name and open it. In the table, it would convert the table to string so writing into file will be easy for string datatype.
    
    newgraphToWrite=input('Enter ur new filename where you want to write that file: ')
    newgraphfile=open(newgraphToWrite,'w')

    for i in range(len(num)):
        for j in range(len(num[i])):
            newgraphfile.write(str(num[i][j])+' ')
        newgraphfile.write('\n')

    newgraphfile.close()






def randomAnimalList():
#this function focuses on generating random animal list which will show output of any random values from Location, climate and plantlife
#using random.randiant() to generalise random number
#first for loop goes into range of animal. Inside that, three tables would be created to randomise any random number and append the item which has that number's index


    Location=['land','freshwater','seawater']
    Climate=['cold', 'tropical', 'arid', 'temperate','polar']
    PlantLife=['conifers', 'mosses','greenalgae', 'flowering', 'ferns']
   
    RandomAnimalTable=[]
    
    
    animal=int(input('Enter the number of animals:(2-10) '))
    for i in range(animal):
        Location1=[]
       
        for j in range(random.randint(1,2)):
            RandomNo1= random.randint(0,2)
            if Location[RandomNo1] not in Location1:
                Location1.append(Location[RandomNo1])


        Plantlife1=[]
        
        for j in range(random.randint(1,2)):
            RandomNo2= random.randint(0,4)

            if PlantLife[RandomNo2] not in Plantlife1:
                Plantlife1.append(PlantLife[RandomNo2])

        Climate1=[]
        
        
        for  j in range(random.randint(1,3)):
            RandomNo3= random.randint(0,4)
            if Climate[RandomNo3] not in Climate1:
                Climate1.append(Climate[RandomNo3])


        print('animal '+str(i))    
        print("Location: " + str(Location1))
        print("Climate: " + str(Climate1))
        print("PlantLife: " + str(Plantlife1))

#In the main table created below, it would be storing all three above tables and items inside them
        table1=[]
        table1.append("animal "+str(i))
        
        for k in range(len(Location1)):
            table1.append(Location1[k])

        for k in range(len(Climate1)):
            table1.append(Climate1[k])

        for k in range(len(Plantlife1)):
            table1.append(Plantlife1[k])

        RandomAnimalTable.append(table1)
        
    return RandomAnimalTable

#randomAnimalList()

 
        







def checkGraph(table):

#this function would be checking whether the graph is connected or not

#first, table would pop all 0 values and table of list is empty.
#using for loop, it will increase vertices by 1 at each iteration. If that item in table is 1 and is not use before, then it would append the column of that table
#When vertices exceeds the length of list, the graph will be connected 

    table.pop(0)

    the_List=[0]
    vertices=0
    for i in range(len(table)):
        vertices+=1
    i=0

    while i<len(the_List):   
        for j in range(len(table[the_List[i]])):
            if table[the_List[i]][j]==1 and j not in the_List:
                the_List.append(j)
        i+=1

    if len(the_List)<vertices:
        return"This graph is not connected"
    
    else:
        return"This graph is connected"



#print(checkGraph(readGraphFromFile()))




def checkIfGraphIsValid(animalList):
#function would check whether the graph is valid
#It will create as much zeros as animals in the list and would print that list randomly.


    size=[]

    for i in range(len(animalList)):
        size.append([0]*len(animalList))

    print(size)

        


#checkIfGraphIsValid(randomAnimalList())








def GreedyApproach():
    


#check if the graph is connected 

    table.pop(0)

    Line=[0]
    vertices=0
    for i in range(len(table)):
        vertices+=1
    i=0

    while i<len(Line):   
        for j in range(len(table[Line[i]])):
            if table[Line[i]][j]==1 and j not in Line:
                Line.append(j)
        i+=1

    if len(Line)<vertices:
        return"This graph is not connected"
    
    else:
        return"This graph is connected"

#check if the graph is valid

    size=[]

    for i in range(len(animalList)):
        size.append([0]*len(animalList))

    print(size)






















    
        




def functionMenu():
#function will ask for different values so that it will be easy for user not to make function call seperatly

    options=1
    
    while options!=8:
        
        print("1. Read file from list")
        print("2. Write current list to file")
        print("3. Generate random Animal List")
        print("4. Read graph from file")
        print("5. Write graph to file")
        print("6. Check if graph is valid")
        print("7. Generate greedy solution")
        print("8. quit")

        options=int(input("Enter the option you want to go with(1 to 8): "))


        if options==1:
            
            AnimalList=getAnimalList(Location, Climate, PlantLife)
            
        elif options==2:
            print("0. Write animal list to file")
            print("9. Write randomely generated animal list to file")
            list=int(input("Enter the list(0 and 9): "))
            while list==0 or list==9:
               
                if list == 0:  
                    AnimalList = getAnimalList(Location, Climate, PlantLife)
                    writeAnimalList(AnimalList)
                    return functionMenu()

                elif list == 9:
                    Random1=randomAnimalList()
                    writeAnimalList(Random1)
                    return functionMenu()

                else:
                    return functionMenu()



        elif options==3:
            random1=randomAnimalList()

        elif options==4:
            readGraphFromFile()
            
        elif options==5:
            c=readGraphFromFile()
            writeGraph(c)

        elif options==6:
            checkIfGraphIsValid(randomAnimalList())

        elif options==7:
            GreedyApproach(randomAnimalList())

        elif options==8:
            break

        else:
            print("Your option doesn't exist")
            
        functionMenu()
        options=input("Enter the option you want to go with now(1-8): ")



functionMenu()








        
#getAnimalList(Location, Climate, PlantLife)
#AnimalList = getAnimalList(Location, Climate, PlantLife)
#writeAnimalList(AnimalList)
##C = readGraphFromFile()
##
##writeGraph(C)
#

