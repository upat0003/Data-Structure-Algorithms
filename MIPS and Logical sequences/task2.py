def Element(the_list): #this function would ask for the size of the list and make the list according to it

    size=int(input("Enter the size of list you want: "))

    the_list=[0]*size   #making the list


    i=0             #index of the list
    while(i<size):  #using while loop
        the_list[i]=int(input("value:"))   #According to size, it's asking for values to enter
        i+=1                               #incrementing the index by 1 at each iteration
    print(the_list)                        #printing the list 
        
    maximum=max(the_list)                  #getting the maximum item from list 
    minimum=min(the_list)                  #taking minimum element  
    Range=maximum-minimum                  #arithmetic operation to find range
    
    print("The range of the list is: " + str(Range) ) #printing the statement with range

    
    
Element(3)                                  #calling the function 
