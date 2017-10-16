def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    sign = 1
    index = 0
    number = 0
    int_max = 2147483647 
    int_min =-2147483648
    bound = -int_min // 10
    str = str.strip()
    length = len(str)
    
    if length == 0:
        return 0  
    if str[0] == '-' and length > 1:
        sign = -1
        #str = str[1:]
        index = 1
    elif str[0] == '+' and length > 1:
        sign = 1
        index = 1
        #str = str[1:]
    
    while index < length:
        if not str[index].isdigit():
            break
        
        digit = ord(str[index]) - 48

        if number > bound or number == bound and  digit > 7:
            if sign == 1:
                return int_max;
            else:
                return int_min;


        number = number*10 + digit
        index += 1
    #print(str)
    return sign*number 


print(myAtoi("-2147483648"))
