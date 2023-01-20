a = (1,)
print(type(a))  # <class 'tuple'>

# PAcking

a = (1, 2, 3)  # packing
(x, y, z) = a  # unpacking
print(x)  # 1
print(y)  # 2
print(z)  # 3


# Astrid

a = (1, 2, 3)  # packing
(x, *z) = a    # unpacking
print(x)       # 1
print(z)       # [2,3]

a = (1, 1, 2, 3)
b = a.count(1)    # Count of 1
c = a.index(1)    # Value in index 1
