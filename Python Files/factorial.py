# a = int(input("Enter a Number : "))
# sum=0
# while a>0:
#     b=a-1
#     sum=a*b
#     a-=1
# print(sum)

# Factorial
a = int(input("Enter a Number : "))
fact = 1
for i in range(1, a+1):
    fact *= i
print(fact)
