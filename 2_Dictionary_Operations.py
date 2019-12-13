# Dictionary operations

# 1.clear 
# 2.copy 
# 3.keys 
# 4.values
# 5.items 
# 6.get 
# 7.pop 
# 8.popitem 
# 9.update 

###################################

# d = {'name':'krishna','id':2336778,'branch':'kadiri',25:500}



# 1.clear : To remove the values in a Dictionary

# d.clear()
# print(d)
##############################################################

# 2.copy: to copy dictionary to another variables    doubt

# d2 = d.copy()
# print(d2)

###############################################

# 3.keys : keys is used to get all values in a dictionary in list format 

# print(d.keys())

##################################

# 4.values : using values we can get the values form dictionary 

# print(d.values())
#######################################3

# 5.itesms: using items we can get keys and values 

# print(d.items())
###############################

# 6.get : get is used to get the values based on keys 

# using get we can provide default value also if key is not present it will return default value

# print(d.get('name','id','branch'))

'''
Error:

  File "1_Dictionary_Operations.py", line 52, in <m
    print(d.get('name','id','branch'))
TypeError: get expected at most 2 arguments, got 3
'''
# print(d.get('id'))
#######################################################3

# 7.pop: using pop we can remove the key and value based on key

# print(d.pop('name'))
# print(d)

###################################################

# 8.popitem:  popitem used to remove the last key and value pair in dicitonary

# print(d.popitem('name'))

'''
Error:
Traceback (most recent call last):
  File "1_Dictionary_Operations.py", line 73, in <module>
    print(d.popitem('name'))
TypeError: popitem() takes no arguments (1 given)
'''
# print(d.popitem())

##############################################################33

# 9.update : update used to concodinate the two dicitonarys

# d.update({'name':'sravani'})
# d.update({'names':['krishna','vasavi']})

# print(d)
##################################################33333

# del : del is used to delete the key and value and entire dicitonary also


# del d['name']
# print(d)
#####################################################33

# Using for loop we can get the keys:

d = {'name':'krishna','id':2336778,'branch':'kadiri',25:500,'languages': ['python','java']}

# for key in d:
    # print(key)

for key, value in d.items():
    print(key,value)

