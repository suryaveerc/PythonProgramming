def recursiveAdd(num):
   
    if num == 0:
        return 0
    else:
        return recursiveAdd(num-1)  + num

def recursiveListRev(lst):
    if lst == []:
        return []
    else:
        remaining = recursiveListRev(lst[1:])
        first = lst[0:1]
   
        result = remaining + first
        return result

def recursiveListRev2(lst):
    
    def helper(index):
        if index == -1:
            return []
        else:
            remaining = helper(index-1)
            first = lst[index]
   
            result = remaining + first
        return result
    return helper(len(lst)-1)

def intpow(num, power):
    
    if(num==0 and power < 0):
        return "infinity" 
    if(power>=0):
        if(power==0):
            return 1
        else:
            return num * intpow(num, power-1) 
    else:
        if(power==0):
            return 1
        else:
            return 1/num * 1/intpow(num, power+1)         

def factorial(num):
    
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
        
def stringLen(string):
    
    if string == "":
        return 0
    else:
        return 1 + stringLen(string[1:])
def swap(chars):
    return chars[1] + chars[0]
def stringSwap(string):
    if string == "":
        return  ""
    elif len(string) == 1:
        return string
    
    else:
        temp = string[0:2]
        
        return swap(temp) + stringSwap(string[2:])
print(stringSwap("suryaveer"))
print(stringLen("hello"))
print(intpow(0, -1))
print(factorial(20))
#print(recursiveListRev([1,2,3]))
#print(recursiveAdd(10))