largest = None
bigemail = None
counts= dict()

files = input()
lines = open(files)

for line in lines:
    if line.startswith("From "):
        strip = line.rstrip()
        words = strip.split()
        email = words[1]
        #print("new ", email)
        if not email in counts:
            counts[email] = counts.get(email,0) + 1
            
        else:
            counts[email] += 1        
        #print("New counts",counts)

    for k, v in counts.items():
        if largest is None or v > largest:
            largest = v
            bigemail = k

print(bigemail, largest)




#{'listya@gmail.com': 2, 'chris@gmail.com':3}



