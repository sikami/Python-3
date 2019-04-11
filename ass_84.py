#open file, read it line by line
#for each line, split()
#for each word, check if word is in list. if not, append
#sort the list

results = list()
library = input()
lines = open(library)
count = 0
for line in lines:
    words = line.rstrip().split()
    for word in words:
        if not word in results:
            results.append(word)
results.sort()
print(results)