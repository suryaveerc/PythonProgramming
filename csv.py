d = list()
with open('a.csv') as data:
    for line in data:
        z,x,c,v,b = line.strip().split(',')
        d= line.strip().split(',')
        print(z,x,c,v,b)
        print(d)