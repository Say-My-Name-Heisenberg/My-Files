fp=open("sample.txt", "w")
emp=int(input("Enter no.of Employee:"))
li=[]
name=""
for i in range(emp):
    name =input("Enter employee name: ")
    li.append(name+"\n")
print(li)
fp.writelines(li)
print("Employee added successfully")

fp=open("sample.txt", "a")
fp.write("hello")



fp=open("sample.txt", "a")
print(fp.read())
fp.close()              #close file 

fp=open("sample.txt", "at")     #before reuse the same file
fp.write("writing data")
fp.close()


import os
os.remove("sample.txt")   #delete the file