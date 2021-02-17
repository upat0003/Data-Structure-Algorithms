def TemperatureFrequencies(the_List):  #this function would make list same as previous tasks
                                       #and would count how many times the particular item is repeated into list using other function 
    size=int(input("Enter the size of list you want: "))
        
    the_List=[0]*size
    
    i=0
    while(i<size):
        the_List[i]=int(input("value:"))         
        i+=1
    return the_List
        

    
               
        
    
the_list= TemperatureFrequencies(2)


def countFrequency(the_list, value):  #this function will match the item one by one with other items 
                                      #and would print how many times it's repeated  
    size=len(the_list)
    i=0
    frequency=0
    
    while(i<size):                      #while loop will check the size with index and returns the frequency
        if(the_list[i]==value):
            frequency=frequency+1
        i+=1

    return frequency




def print_list():                       # this function would print the list by how many times particular number is written
    frequency=min(the_list)             
    while(frequency<=max(the_list)):    # while loop to make sure minimum of the list is less than maximum element
        result= countFrequency(the_list, frequency)  # calling the upper dunction and store it into result
        if(result>0):  #if the number of times it's printed is greater than 0, it'll print the statement
            print(str(frequency) + " appears " + str(result) + " times")  #printing the statement for the required result
        frequency+=1                                                      # incrementing the frequency

print_list()            #calling the function to print it
                
              
            
          
    
