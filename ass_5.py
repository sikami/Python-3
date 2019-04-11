# prompts user for integer
# program will exit once user enters done
#if enter alfabet, catch with try/except, ignore numbers continue;

smallest = None
largest = None 

count = 0

while True:
    user_number = input("Please enter a number:") 
    
    if user_number == "done":
       break
    try:
       float_number = float(user_number)
    except:
       print("Invalid Input")
       continue

    #count = count + 1
    # 
    for num in [float_number] :
        if float_number >largest :
            largest = float_number
        elif float_number < smallest :
            smallest = float_number
    
    print("Maximum is", largest)
    print("Minimum is", smallest)
    

    
    

     

