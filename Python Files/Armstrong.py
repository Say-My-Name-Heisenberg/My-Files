#153, 370, 371, 407, 1634, 8208, 9474, 54748,
while True:
    a = int(input("Enter a Number : "))
    temp = a
    rem = 0
    sum = 0
    while a > 0:
        rem = a % 10
        sum += rem*rem*rem
        a = a//10
    if temp == sum:
        print("Armstrong")
    else:
        print("Not Armstrong")
