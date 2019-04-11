a = input()
if len(a) < 1:
   a = "mbox-short.txt"

lines = open(a)
dates = dict()
list_dates = list()

for line in lines:
    if line.startswith("From "):
        words = line.split()
        num = words[5]
        numsplit = words[5].split(":")
        hour = numsplit[0]

        if not hour in dates:
            dates[hour] = dates.get(hour,0) + 1
        else:
            dates[hour] += 1
      
for k,v in dates.items():
    list_dates.append((k,v))

temp = sorted(list_dates)

for k, v in temp:
    print(k,v)