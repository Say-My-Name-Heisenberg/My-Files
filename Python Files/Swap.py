from pkg_resources import cleanup_resources


a=100
b=200
a,b=b,a
print("a:",a)
print("b:",b)