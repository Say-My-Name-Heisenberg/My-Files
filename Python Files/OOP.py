# PROGRAMMMING PARADIGM DEFINED

# What is a programming paradigm?
# A programming paradigm is the classification, style or way of programming.
# It is an approach to solve problems by using programming languages.
# Depending on the language,the difficulty of using a paradigm differs.


# OOP

# its aprograming pardigm thats provides means of structuring progrms so that
# properties and behavior are bundled into individual objects

# features
#                ---------
# 1.class
# 2.object
# 3.inheritance
# 4.Encapsulation
# 5.Abstraction
# 6.Polymorphism

# Class :-blueprint of an object,data type of an object.
#               class-syntax:
#                     class class_name:
#                           #members of class

# Object :- while class is blueprint an instance is an object that is build from a class and contains raw data
# class laptop:
#     ram=4
#     rom=128
#     def __init__(self):
#         print ("Object Created")
#     def booting(self):
#         print("Booting....")

# dell=laptop()
# dell.__init__()
# dell=laptop()          #default constructor
# print(dell.ram)
# print(dell.rom)
# dell.booting()
# print(dell)

# hp=laptop()
# print(hp.ram)
# print(hp.rom)
# hp.booting()
# print(hp)

# construct is a method that meant for instanciation with initialization(assingning a specific memory location)
#       1.Default Constructor     -> def __init__(self):     __
#       2.Parametrized Constructor



class laptop:
    processr = "Intel i3"  # class attributes

    def __init__(self, a, b):
        self.RAM = a  # instance attribute
        self.ROM = b
        print("Object Created", self)

    def booting(self):
        print("Booting....on "+str(self.RAM)+"GB RAM")


dell = laptop(4, 64)
print(dell.RAM)
print(dell.ROM)

mac = laptop(2, 32)
print(mac.RAM)
print(mac.ROM)

dell.booting()
mac.booting()

# Inheritance :- its a propertie of a class which can show attributes and context from another class

# Types of Inheritence
# 1.Single Inheritence
# 2.Multiple Inheritence
# 3.Multi-Level Inheritence
# 4.Hierarchy Inheritance


class Parent:
    name = "parents name"

    def parent_method(self):
        print("parent Method")


p = Parent()
print(p.name)
p.parent_method()


class child(Parent):  # eg.Single Inheritence
    pass


c = child()
print(c.name)
c.parent_method()

# ----------------------------------------------------------


class Parent1:
    name1 = "parent1 name"

    def parent_method1(self):
        print("parent1 Method")


class Parent2:
    name2 = "parent2 name"

    def parent_method2(self):
        print("parent2 Method")


class child(Parent1, Parent2):  # eg.Multiple Inheritence
    pass


c = child()
print(c.name1)
print(c.name2)
c.parent_method1()
c.parent_method2()

# ---------------------------------------------


class A:
    aname = "a"


class B(A):
    bname = "b"


class C(B):
    pass


c = C()  # Multi Level Inheritence
print(c.aname)
print(c.bname)
b = B()
print(b.aname)


# -----------------------------------------------------

class Parent:
    name = "Parent"


class Child1(Parent):
    pass


class Child2(Parent):
    pass


class Child3(Parent):         # Hierarchy Inheritance
    pass


c1 = Child1()
c2 = Child2()
c3 = Child3()

print(c1.name)
print(c2.name)
print(c3.name)


# -----------------------------------------------------

class A:
    a = "nam of a"


class B(A):
    b = "name of b"


class C:
    c = "name of c"


class D(B, C):
    d = "name of d"


class E(D):
    e = "name of e"


e = E()
print(e.a)
print(e.b)
print(e.c)
print(e.d)
print(e.f)


# -----------------------------------

class Parent:
    a = "apple"

    def fun(self):
        print(self.a)   #
        return "Parent Function"


class Child(Parent):
    def join_str(self):
        a_val = super().a
        fun_val = super().fun()
        print(a_val+fun_val)


c = Child()
c.join_str


# Encapsulation :- its wrappping of data into a single unit

# its component that specifies the access of a specific class member
# Access Specifiers :
# 1.Public
# 2.Protected
# 3.Private

class A:
    a = 10


class B(A):
    pass


class C(B):  # Public Access Specifier
    pass

    # Protected
    # the members of class data protected are only accessible to a class derived from it

    # Private
    # a class member defined as private member consiterd to be only accesible in yhe same class its self


class A:
    __a = 10

    def __fun(self):
        print("Private")

    def ex(self):
        print(self.__a)
        self.__fun()


ob = A()
ob.ex()
# Abstraction :- it means showing relevent data while hiding irrelevent data
# used to hide internal functionality to user , user knows what function does and not how it does
# in python abstraction used to hide irrelvent data inorderd to reduce complexcity and also to enhance application efficiency
# in python we can achive abstraction through abstract classes
# a class consisit of 1 or more abstract method is called abstract class
# abstract method doesnt contain implementation
# Abstract class is considerd as the blueprint  of another classes
# when we create an abstraction class an inherit into another class then the derived class must cintain every abstract methods that define in the
# for a class to be an abstract class
# :- FIRST it must be a child of A B C(abstract base class)
# :- it must contain atleast one abstract method
# :- the abstract method should be decoreted using abstractmethod decorated
from abc import ABC, abstractmethod

class Main(ABC):
    @abstractmethod
    def fun(self):
        pass
    @abstractmethod
    def addd(self):
        pass
    def norm(self):
        print("Normal function")

class child(Main):
    def speed(self):
        print("speed")
        super().norm()
    def fun(self):
        print("Ab method defined in method")
    def addd(self):
        print("hi")


m = child()
m.speed()




# An abstract class cannot be instantiate
# childern classes of abstract class must contain / use each and evry  abstract method defined in abstract class
# abstrcat class can contain both abstract method and normal method

# DECRATOR :- this are special method used to add additional meaning to another method to another function


# Polymorphism :- it means a single begins having may forms
