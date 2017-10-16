data = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
evens = [num for num in data if not num % 2]
print(evens)

data = [ 1, 'one', 2, 'two', 3, 'three', 4, 'four' ]
words = []
words  = [wrd for wrd in data if isinstance(wrd,str)]
print(words)

data = list('So long and thanks for all the fish'.split())

title = [word.title() for word in data]
print(title)