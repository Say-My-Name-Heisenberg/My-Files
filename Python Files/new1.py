# Regular Expression/Regex:

#  its a sequence of character that form a search pattern .
# it can be used to check if a string contain specifed search pattern
# python has build in  package for regex that is  re.


# re Functions :

#1.findall() :- returns a list contain all matches
#2.search() :- returns a match object if there is a match anywhere in the string.
#3.split()  :- returns a lsit were the string has been splite at each match.
#4.sub()   :- replaces matches with the text of your choice


import re


txt1 ="a ab abc abcd"
fin= re.findall("ab",txt1)
print(fin)

txt2 = "The end"
ser=re.search("^The .*$",txt2)
print(ser)

print(ser.span())   #INDEX OF FIRST SEARCH STRING
print(ser.string)    #RETURN STRING
print(ser.start())     #INDEX OF start
print(ser.end())   #INDEX OF end


txt3 ="the rain in spain"
spl=re.split(" ",txt3)
print(spl)


txt4="arjun ck"
sub=re.sub(" ","-",txt4)
print(sub)

