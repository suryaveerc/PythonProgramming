def changecase(string):
    print("In Changecase: ", string)
    def camelCase(string, toUpper):
        print("In Camelcase: ", string)
        if len(string) == 0:
            return ""
        elif toUpper== True:
            print("==> TO UPPER <==", string)
            result = string[0].upper()
            remaining = string[1:]
            return result + camelCase(remaining, False)
        else:
            print("--> to lower <--", string)
            result = string[0].lower()
            remaining = string[1:]
            return result + camelCase(remaining, True)            
    if string[0].isupper():
        return camelCase(string, False)
    else:
        return camelCase(string, True)
print(changecase("suRyVAeeR"))