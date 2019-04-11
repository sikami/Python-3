a = input("Enter file name:")
b = open(a)

for i in b:
    i = i.upper().strip()
    print(i)