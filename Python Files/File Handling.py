# Python File Handling

# syntax:
#        file_pointer_var=open("filename","modes")

# Modes

#         "r" - read mode
#         "w" - write mode
#         "a" - append mode
#         "x" - create mode

#         "w+" - write and read mode

z = open("sample.txt", "w")
# read = z.read()
# print(read)


# read1 = z.readlines()
# read2 = z.readline()
read3 = z.writelines("off")   

print(read3)
