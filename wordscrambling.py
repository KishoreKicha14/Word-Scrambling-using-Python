import random
def scword(words):
    lis=list()
    for letters in words:
        lis.append(letters)
    if(words.endswith(('.',',','?','!',';'))):
           length=len(words)-1
    else:
           length=len(words)
    for j in range(1,length-1):
           r=random.randint(j,length-2)
           if(j==r):
               r=random.randint(j,length-2)
           temp=lis[j]
           lis[j]=lis[r]
           lis[r]=temp
    words=''.join(lis)
    return(words)    
def sc(sentences):
    lis=list()
    for words in sentences:
        words=scword(words)
        lis.append(words)
    return(lis)  
with open("hello.txt", 'r') as f:
   data = f.readlines()
file = open('testfile.txt','w') 
for line in data:
   sentences = line.split()
   sentences=sc(sentences)
   str1 = ' '.join(sentences)
   file.write(str1)
file.close()
