import re
#Task A
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
no_hypen=re.findall('[a-zA-Z0-9]?-[a-zA-Z0-9]',data)
print("Number of the hypens in the corpus is : ",len(no_hypen))
no_digit=re.findall('\d',data)
print("Number of the numbers in the corpus is : ",len(no_digit))

res = data.split()
word_vowel=[]
for y in res:  
    no_vowel=re.search('^[aeiouAEIOU][A-Za-z0-9_]+',y)
    # print(no_vowel)
    if(no_vowel!=None):  
         word_vowel.append(no_vowel.group())
print('The words starting with vowels are : ',word_vowel[:20])  
romans=[]
for y in res: 
    no_roman=re.match('^M{0,3}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$',y)
    if(no_roman!=None):
        romans.append(y)
print('The roman numbers in corpus are : ',set(romans))
f.close()

#Task B