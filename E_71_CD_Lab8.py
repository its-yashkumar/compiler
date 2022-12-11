import re
f = open("task1.txt", "r", encoding="utf8")
count_the=0
for x in f:
    if(re.search('the',x)): 
        count_the+=1
print("Number of the pronoun 'the' in the corpus is : ",count_the)
f.close()


fin = open("task1.txt", "rt",encoding="utf8")
#read file contents to string
data = fin.read()
y=(re.search('^i$',data))
#replace all occurrences of the required string
if not y == None:
     data = data.replace(y, 'python')
fin.close()
fin = open("task1.txt", "wt",encoding="utf8")
#overrite the input file with the resulting data
fin.write(data)
#close the file
fin.close()

f = open("task1.txt", "r", encoding="utf8")
data=f.read()
no_quotes=re.findall('“(.+?)”',data)
print("Number of the quotes in the corpus is : ",len(no_quotes))
f.close()
