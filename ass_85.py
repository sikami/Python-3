#open file and read
#if name starts from 'From ', extract 2nd word
#print words

a = input()
if len(a) < 1:
    a = "mbox-short.txt"

fname = open(a)
count = 0
emails = list()

for line in fname:
    if line.startswith("From "):
        words = line.split()
        emails.append(words[1])
        count += 1

for email in emails:
    print(email)
print("There were", count, "lines in the file with From as the first word")

        