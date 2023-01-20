
class employee:
    def __init__(self):
        self.name = input("name:")

    def __str__(self):                      # Python __str__()
        return self.name                    # -----------------
        # This method returns the string representation of the object.
        # This method is called when print() or str() function is invoked on an object.
        # This method must return the String object

    def __del__(self):
        print("Object DEleted")  #In Python, the __del__() method is referred to as a destructor method. 
        # It is called after an object's garbage collection occurs, 
        # which happens after all references to the item have been destroyed. 


ob = employee()
ob1 = employee()
del ob1    #manually calling destructor
print(ob)
print(ob1)
