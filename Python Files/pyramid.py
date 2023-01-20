#For loop
#---------

# a = int(input("Enter a Number : "))
# for i in range(a):
#     print(i * "*")


# a = int(input("Enter a Number : "))
# for i in range(a):
#     print(a * "*")
#     a-=1


# a = int(input("Enter a Number : "))
# for i in range(0,a):
#     for j in range(i):
#         print(i,end="")
#     print(" ")


# #While
#--------

# a = int(input("Enter a Number : "))
# i=0
# while i<=a:
#     print(i * "*")
#     i+=1

# a = int(input("Enter a Number : "))
# i=0
# while i<=a:
#     print(a * "*")
#     a-=1
    
a = int(input("Enter a Number : "))
for i in range(a):
    print(" "* a,i*"* ",end =""+"\n")
    a -=1


# a="apple is red"
# b={1:"apple",2:"orange",3:"kiwi"}
# for i in b:
#     print(b[i])-