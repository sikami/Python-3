score = input("Enter Score: ")
try: 
    a = float(score)
except:
    print("Error")
    quit()

if a >= 0.9 :
    print("A")
elif a >= 0.8 :
    print("B")
elif a >= 0.7 :
    print("C")
elif a >= 0.6 :
    print("D")
else :
    print("F")
