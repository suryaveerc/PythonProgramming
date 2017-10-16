
vowels = ['a','e','i','o','u']
found = {}
string= "Suryaveer"
count=0
for i in string:
    if i in vowels:
        #below two lines can be replaced by found.setdefault(i,0)
        if i not in found:
            found[i]=0
        found[i] = found[i]+1

            

print(found)

for k,v in found.items():
    print(k,":",v)
print("String: ", string , " contains ", count , " unique vowels")

vowelsSet = {'a','e','i','o','u'}
print("Set union: ",vowelsSet.union(set(string)))
print("Set difference: ",vowelsSet.difference(set(string)))
print("Set difference: ",set(string).difference(vowelsSet))
print("Set intersection: ",vowelsSet.intersection(set(string)))
print(vowelsSet)

def panic():
    phrase = "Don't panic!"
    plist = list(phrase)
    print(phrase)
    print(plist)
    for _ in range(4):
        plist.pop()
    plist.remove("D")
    plist.extend([plist.pop(),plist.pop()])
    plist.remove(" ")
    plist.insert(plist.index("'")," ")
    plist.remove("'")
    print(plist)
    
    new_phrase = ''.join(plist)
    print(plist)
    print(new_phrase)  
    


