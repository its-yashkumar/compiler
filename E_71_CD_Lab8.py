import re
f = open("task1.txt", "r", encoding="utf8")
for x in f:
    y=(re.search('the',x))
    print(y)
f.close()