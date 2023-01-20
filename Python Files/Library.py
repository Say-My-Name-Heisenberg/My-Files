# bin = int(input("-:"))

# temp = bin
# rem, dec = 0, 0
# pos = 0
# while temp > 0:
#     rem = temp % 10
#     sq = rem*(2**pos)
#     dec += sq
#     pos += 1
#     temp = temp//10
# print(dec)

temp = int(input("Enter a decimal number to convert to binary:-"))


def bin(n):
    rem, dec, pos = 0, 0, 0

    while n > 0:
        rem = n % 10
        sq = rem*(2**pos)
        dec += sq
        pos += 1
        n = n//10
    return dec


print(bin(temp))
