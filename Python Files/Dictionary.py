# Orderd after python 3.6 version

dict = {1: "apple", 2: "orange"}
b = dict.get(1)
print(b)  # apple

c = dict.keys()
print(c)  # dict_keys([1, 2])


d = dict.values()
print(d)  # dict_values(['apple', 'orange'])

# returs list of tuples were each tuple is a key value pair from specifide dictionary
e = dict.items()
print(e)         # dict_items([(1, 'apple'), (2, 'orange')])

dict.update({1: "Banana"})  # edit dictionary or add new key value pair
print(e)                   # dict_values(['Banana', 'orange'])

dict.pop(1)                 # remove value by calling key
print(e)

f = dict.popitem()      # remove last key,value pair
print(f)
