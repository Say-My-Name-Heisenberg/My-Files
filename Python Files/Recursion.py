# Fibinocci Series
def fib(val):
    if val == 0:
        return 0
    if val == 1:
        return 1
    elif val > 1:
        return (fib(val-1))+(fib(val-2))


val = int(input("Enter Limit:"))
for i in range(val):
    print(fib(i), end=",")
