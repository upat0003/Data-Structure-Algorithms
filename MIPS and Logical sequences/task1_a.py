def is_leap_year(year):     #function which will check if the inputted number is leap year
    

    year=int(input("Enter the year:")) #asking to enter the year to compare

    if(year<1582): 
        print("Enter number greater than 1581") #if the condion meets, it will print the following statement
    else:

        if((year%4==0) and (year%100!=0) or (year%400==0)):
            print("Is leap year")  
            return True
        
        else:
            print("Is not a leap year")
            return False


is_leap_year(2000)    # calling the function to run the programme
