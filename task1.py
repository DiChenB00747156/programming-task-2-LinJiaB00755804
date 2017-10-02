import string
with open('Crime.csv','r') as fin:
    mylist = []
    mydic1 = {}
    mydic2 = {}
    for line in fin:
        clean_line = line.strip(string.whitespace)
        new_clean_line = clean_line.strip()
        wordlist = new_clean_line.split(',')
        mydic2[wordlist[-1]]=wordlist[-2]
        if wordlist[-1] in mydic1:
            mydic1[wordlist[-1]] +=1
        else:
            mydic1[wordlist[-1]] = 1
    for count,name in sorted([ (value,key) for (key,value) in mydic1.items()], reverse = True):
        mylist.append(name)
        mylist.append(mydic2[name])
        mylist.append(count)
        
    print(mylist)
            
    


