# Duplicate

# a = [1, 2, 2, 1, 10, 10, 2, 10, 2, 1, 5, 4, 5,6 ]

# b = a.sort()
# z = []
# print(a)

# for i in a:
#     if i in z:
#         continue
#     z.append(i)

# print(z)
# ----------------------#

# Comprehension (dictionary)
# a = [1, 1, 2, 2, 1, 3, 2, 3, 4, 4, 5, 6, 5, 4, 5, 3, 2, 4, 2, 5, 6]
# z = []
# m = dict()
# for i in a:
#     if i in z:
#         continue
#     z.append(i)
#     m[i] = a.count(i)
# print("Delete Duplicates", z)
# print(m)


a = [1, 2, 2, 1, 10, 10, 2, 1, 5, 4, 5, 6]
b = []
c = {}
d = 0
for i in a:
    if i not in b:
        d = a.count(i)
        c.update({i: d})
        b.append(i)
print(b)
print(c)
