from multipledispatch import dispatch
  
@dispatch(int,int)
def product(a,b):
    result = a*b
    print(result);
  
@dispatch(int,int,int)
def product(a,b,c):
    result  = a * b * c
    print(result);
  
@dispatch(float,float,float)
def product(a,b,c):
    result  = a * b * c
    print(result);
  
product(5,6)
product(2,3,2) 
product(2.2,3.4,2.3)
