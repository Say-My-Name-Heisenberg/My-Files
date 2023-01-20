# word = input("Enter a palindrome:")
# if word == word[::-1]:
#     print("its palindrom")
# else:
#     print("Not palindrom")


word = input("Enter a palindrome:")
pal = ""
for i in word:
    pal = i + pal
if word == pal:
    print("its palindrom")
else:
    print("Not palindrom")