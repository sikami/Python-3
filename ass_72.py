#prompts file name
#open file name
#iterate through file
#find lines: X-DSPAM-Confidence:    0.8475
#count lines
#convert into float all the lines
#compute the average 

fname = input()
fopen = open(fname)
count = 0
total = 0
for i in fopen:

    if i.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        a = i.find("0")
        b = a + 6
        c = float(i[a:b]) 
        total = total + c
print("Average spam confidence:", total/count)
