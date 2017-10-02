import string
with open('Crime.csv','r') as fin:
    mylist = []
    mydic = {}
    for line in fin:
        clean_line = line.strip(string.whitespace)
        new_clean_line = clean_line.strip()
        wordlist = new_clean_line.split()
        if len(wordlist)>3:
            s = wordlist[-3].split()
            d = wordlist[-2]
        if wordlist[-1] in mydic:
            mydic[wordlist[-1]] +=1
        else:
            mydic[wordlist[-1]] = 1
    for count,name in sorted([ (value,key) for (key,value) in mydic.items()], reverse = True):
        if ',' in name:
            t = name.split()
            print(t[-1],t[-2],count)
        elif ',' in wordlist[-3]:
            print(s[2],d,name,s[1],count)
    

    
