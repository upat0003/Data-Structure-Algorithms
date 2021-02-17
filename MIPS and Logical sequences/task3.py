def TemperatureExceed(the_list, Target):  #function would get argument of the_list and Target and would count how many times Target has exceeded the list elements

    size=int(input("Enter the size of list you want: "))  #it will ask for elements in the list
        
    the_list=[0]*size
    new_list=[0]*0
    
    i=0
    while(i<size):
        the_list[i]=int(input("value:"))

        if(the_list[i]>Target):
            new_list.append(the_list[i])

        i+=1

    Target=int(input("The comparison temperature: "))  #it would ask for the temperature to compare


    print("Temperature was exceeded " + str(len(new_list)) + " time(s)") #printing the statement containing how many times Target is exceeded
        

    
               
        
    
TemperatureExceed(2,34) # calling the function
