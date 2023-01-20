x = int(input("Enter A Number: "))

for i in range(x+1):
    x//i

if x//x==1 and x//1==x:
    print("The given Number is Prime")
else:
    print("Not Prime")