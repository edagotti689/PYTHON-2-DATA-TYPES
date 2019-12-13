'''
String Operations:
1.Capitalize 
2.Count
3.Find
4.Index 
5.Islower
6.Isupper
7.Lower 
8.Lstrip
9.Rstrip
10.Strip
11.Replace 
12.Split 
13.Type 
14.Upper 
15.Join
16.Title


'''
# 1.Capitalize: To convert only first charecter into upper letter in a string.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# split::
# s = 'krishna,raju,balaji'

# print(s.split(','))

# output -  we will get output in list for mat 

# Output  ==  ['krishna', 'raju', 'balaji']

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

''''
# 15.join :
# Ex: 1

s = 'this','is', 'a', 'Python', 'world'

join = ':'.join(s)
print(join)

Ex: 2
s = 'this','is', 'a', 'Python', 'world'

join = '='.join(s)
print(join)

Ex: 3

s = 'this','is', 'a', 'Python', 'world'

join = '%'.join(s)
print(join)

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Errors:
1.  File "Practice.py", line 6, in <module>
    print(s.rplace('raju','AshaRani'))
AttributeError: 'str' object has no attribute 'rplace'

?????????????????????????????

2.  File "Practice.py", line 6, in <module>
    print(s.index('z'))
ValueError: substring not found

????????????????????????????????


'''
