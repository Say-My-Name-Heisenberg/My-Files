#Local Scop

#a variable created inside a function  belongs to  the local scop of that function & can only used inside inside that function
def fun():
    a=10
    print(a)
fun()
print(a)

    #a variable created in the main body of the python code is a global variable and belons to global scop
# global variables are avialable within ant scop , global and scop
# we can use global keyword to give global scop for a variable which is in local scop
