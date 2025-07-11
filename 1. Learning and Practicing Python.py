
# +----+ \     / ---+--- |    | +----+ |\     |
# |    |  \   /     |    |    | |    | | \    |
# |    |   \ /      |    |____| |    | |  \   |
# +----+    |       |    |    | |    | |   \  |
# |         |       |    |    | |    | |    \ |
# |         |       |    |    | +----+ |     \|


"""
High level programming language
Free and open source
Simple and easy to use
Case sensitive language

Developed by 'Guido Van Rossum'
"""

#########################################
# Important terms related to python :-- #
#########################################

##################################################################################################################################################
"""
VARIABLES

The names given to different memory locations.
Also called identifiers.

Example
Name = “Rohan”
'Name' variable is assigned with Rohan as value
"""
##################################################################################################################################################
"""
KEYWORDS

Special words that perform some special tasks in a program.

for      | while    | if       | elif     | else
True     | False    | break    | continue | None
not      | and      | or       | pass     | def
return   | lambda   | try      | except   | finally
import   | from     | as       | class    | is
in       | await    | yield    | with     | del
global   | nonlocal | except   |
"""
##################################################################################################################################################

"""
COMMENTS

Non-executable statements/part of code that can be seen by it's programmer/coder only.

# is used for single line comments and """ """" is used for multi-line comments.
"""

#A variable can’t start with a number. It can’t be a Keyword as well. And it also cant have special characters like # , “ , / ……etc.

##############
# Data types #
##############

##################################################################################################################################################
"""
INTEGER

Positive and negative whole numbers and zero.

Example:--
-29 , -5 , 0 , 76 , 921 ...... etc
"""
##################################################################################################################################################
"""
FLOAT NUMBERS

Numbers in decimal form.

Example:--
71.5 , 25.79 , 5.00……etc
"""
##################################################################################################################################################
"""
BOOLEANS

'True' and 'False'
"""
##################################################################################################################################################
"""
STRINGS

“Hi, my name is Rohan and I am 18 years old.”

Immutable 

Written in between " " or ' ' or ''' ''' according to need
"""
##################################################################################################################################################
"""
LISTS

[“Rohan”, 18, 2005, “Hi”]

Mutable

Collection of multiple Strings and numbers in a square bracket[ ]
"""
##################################################################################################################################################
"""
TUPLES

(“Rohan”, 18, 2005, “Hi”)


Immutable

Collection of multiple Strings and numbers in  parentheses( )
"""
##################################################################################################################################################
"""
DICTIONARIES

{'name: 'Rohan', 'age':18, 'Year':2024}

Key:Value pairs

Does not allow more than 1 key    of same type

Values are Mutable

Keys and values could be anything (like Tuples, integers, lists, string, Boolean……etc).

Keys are Immutable

Dictionaries are unordered
"""
##################################################################################################################################################
"""
SETS

Collection of unordered items.

Each element must be unique and immutable i.e. no immutable data type can be stored in it and multiple same items will only be counted once like, {1,2.4,3,3,4} --> {1,2.4,3,4}

Integers      Floating Numbers      Boolean      String      Tuple

Sets are mutable i.e. elements can be added or removed, but its elements are immutable i.e. no 2 elements can be same (unique).
"""
##################################################################################################################################################
"""
None

A=None

This represents that A is an empty variable(no value assigned to it).
"""
##################################################################################################################################################
"""
MUTABLE AND IMMUTABLE DATA TYPES

+----------------------------+---------------------------+
|          Mutable           |         Immutable         |
+----------------------------+---------------------------+
| Values can be changed      | Values can't be changed   |
+----------------------------+---------------------------+
| Example:--                 | Example:--                |
| Lists                      | Strings                   |
| Dictionaries               | Tuple                     |
| Sets                       |                           |
+----------------------------+---------------------------+
"""
##################################################################################################################################################


#############
# OPERATORS #
#############

##################################################################################################################################################
"""
>>> ARITHEMATIC OPERATOR

1. A+B      Addition    
2. A-B      Substraction
3. A*B      Multiplication
4. A/B      Divide and result in float form
5. A**B     A powered up to B times
6. A//B     Divide and result in nearest smaller integer form
7. A%B      Remainder
"""
##################################################################################################################################################
"""
>>> RELATIONAL OPERATOR

1. ==       Equal
2. !=       Not equal
3. <        Less than
4. >        More than 
5. <=       Less than and equal to
6. >=       More than and equal to
"""
##################################################################################################################################################
"""
>>> ASSIGNMENT OPERATOR

1. A+=B     Addition
2. A-=B     Subtraction
3. A*=B     Multiply
4. A/=B     Divide and give result in float form
5. A%=B     Remainder
6. A**=B    A power up to B 
7. A//=B    Divide and give result in nearest smaller integer

# They save the result as the new value of A.
"""
##################################################################################################################################################
"""
>>> LOGICAL OPERATOR

1. not    Reverses the result i.e. 'True' to 'False' and 'False' to 'True'
2. and    Gives False if there is even one of it in options
3. or     Gives False if there is even one of it in options
"""
##################################################################################################################################################


####################
# print() commands #
####################

print("HelloCoders")
      
print("Hello","Coders")                   # Here ',' adds a space in between 2 strings - 'Hello' and 'Coders'

print(29)                                 # No need of " " for print the Data Type

print(21+19)

Name="Myself"
Age=18

print(Name)

print(Age)

print(Name,Age)

print("I'm",Name, "and my age is",Age,".")

print(Name,end="$")                        #end is \n by default
print(Age)

print(Name,Age,sep='\t')                   #sep is“ ” by default

# String Formatting
""" 1st Method """
name = "Alice"
marks = 85
print("{}'s marks: {}".format(name, marks))

""" 2nd Method """
name = "Alice"
marks = 85
print(f"{name}'s marks: {marks}")

""" 3rd Method """
name = "Alice"
marks = 85
print("%s's marks: %d" % (name, marks))

""" 4th Method """
print("{0}'s marks: {1}".format(name, marks))


##################################################################################################################################################


##############
# Data Types #
##############

A='Hello'
B='70'
C=23
D=13.05

print(type(A))

print(type(B))

print(type(C))

print(type(D))
##################################################################################################################################################


###################
# Type Conversion #
###################

print(C+D)                  #Integer data type is converted into Float Type

# print(B+D)                #ERROR because B is string type

M=float(B)                  #Converted manually
print(M+D)

# print(A+C)                #ERROR because A is string type

# N=float(A)                #ERROR because A is string type and can’t be converted because it is not compatible for conversion
##################################################################################################################################################


#################
#input() command#
#################

A=input("Enter your name:")           #input() will insert string type only
print("Name:",A)
#----------or----------#
print(f"Name:{A}")                    # Speciality in V S Code

# Others
"""
* int(input()) is for integer type input only
* float(input()) is for float number type input only
"""
##################################################################################################################################################


a=round(6.4+9.45)                  # Gives round integer data type figure of 'a'
print(a)                           # A number x.5 will return x+1

#########################################################################
#For printing a statement for a desired number of times using while loop#
#########################################################################

Count=1
while Count<=3:
    print('Yo')
    Count+=1


#####################################
#For printing 'Its (number-->1 to 4)#
#####################################
 
i=1
while i<=4:
    print("Its",i)
    i+=1


##################################################################################################
#---------------------------------------For printing a statement infinite times using while loop #
#---------------------------------------while True:                                              #
#---------------------------------------    print('Hi')                                          #
##################################################################################################


##########################
# if-elif-else statement #
##########################

"""
if (Condition1):
      Statement1
elif (Condition2):
      Statement2
else (Condition3):
      Statement3

Which statement will execute depends on which condition is met by the  variable or something
"""

"""
statement1 if condition1 else condition2 if condition2 else statement3 
"""


##################
# Error Handling #
##################

# Raising Custom Errors

# Structure
"""
raise <Error Type>("Message")
"""

a-int(input("Enter a number between 1 and 10 : "))
if a<1 or a>10:
    raise ValueError("You Have an Error Here")


#############################
# try-except-else statement #
#############################

"""
try:
    (Usually taking some input)
except <error name>:
    (Message in case of error)
else:
    (Rest of the code)
"""


###############
# Enumeration #
###############

marks=[1,2,4,6,8,9]
for index,mark in enumerate(marks):         # Enumerate function tells the value of index of any list / tuple .... along its value
    print(mark)                             # You can put the
    if index == 3:
        print("Index 3")


#############################
# if __name__ == "__main__" #
#############################
"""
in first file - RJ.py
"""
def welcome():
    print("Hello Fellas")
print(__name__)
if __name__=="__main__":
    welcome()

"""
in second file - main.py
"""
import RJ
RJ.welcome()                                 # Will print 'Hello Fellas' due to __name__=="__main__"
                                             # Else it will print 'Hello Fellas'
                                             #                    'Hello Fellas'


###################
# Lambda Function #
###################
double = lambda x : x*2
list=[1,2,3]
for i in list:
    print(double(i))

avg = lambda x, y, z: (x + y + z) / 3
nums = [1, 3, 5]
print(avg(*nums))


##########################
# Map, Filter and Reduce #
##########################
def cube(x):
    return x*x*x
l=[1,2,3,4,5,4,6]

# MAP
# Instead of using
"""
newl=[]
for item in l:
    newl.append(cube(item))
print(newl)
"""
# Use
newl = list(map(cube,l))
print(newl)

# FILTER
def fil_fn(a):
    return a>2

newnewl = list(filter(fil_fn,l))
print(newnewl)

# REDUCE
from functools import reduce
num = [1,2,3,4,5]
def sum(x,y):
    return x+y

sum = reduce(sum,num)


##################################
#Printing the elements in a list #
##################################

List=[1,2,3,4]
for el in List:
    print(el)


#####################################################
#Printing the elements in a list and Over at the end#
#####################################################

for el in List:
    print(el)
else:
    print('Over')


#################################
#Finding an element from a tuple#
#################################

Num=(1,3,5,8,6,9,11)
X=int(input("Enter the number:"))
i=0
while i<len(Num):
    if Num[i]==X:
        print('found')
        break
    else:
         print('searching')
    i+=1


####################################################
#Code for printing all odd numbers between 1 to 10 #
####################################################

i=1
while i<=10:
    if (i%2!=0):
        print(i)
    i+=1


########################################
#Code to find a character from a string#
######################################## 

A="Rohan"
for I in A:
    if I=='h':
        print('Found')
        break
    else:
        print('Search')


###################################################
#Printing numbers at an interval of 2 from 1 to 15#
###################################################

for I in range(1,15,2):
    print(I)


###########
# Strings #
###########

print('Hello'+'Coders')

Str="Welcome Coder:)"
print(len(Str))

print('Hi \nBro')                          # \n => New Line

print('Hi \tBro')                          # \t => Tabular Space

S='HELLO BRO'                              # H E L L O   B R O
print(S[6])                                # 0 1 2 3 4 5 6 7 8   <=Index Value

print(S[1:7])                              # Slicing

#str[0:5] is same as str[:5]
#str[3:len(str)] is same as str[3:]

S.endswith('O')                            # Checks if the string ends with a particular letter/Character/set of them

str="missisipi"
print(str.capitalize())                    # Capitalizes the first letter of the string

print(str.replace('pi', 'ppi'))            # Replaces the first presence of 'pi' to 'ppi'

print(str.find('si'))                      # Finds the first index value of occurence of 'si'

print(str.count('si'))                     # Counts the number of times 'si' occurs in the string 

S1="NEGATIVE"                  # N  E  G  A  T  I  V  E
print(S1[-6:-2])               #-8 -7 -6 -5 -4 -3 -2 -1

name="           Virat Kolhi Sir              "
print(name.strip())                        # Replaces the space from start and end of the string

name="virat kolhi sir"
print(name.title())                        # Capitalizes the first letter of every word of the string


#########
# LISTS #
#########

List=['Senenteen',10,2.4,76]

#Empty List : []
#Single element list =[23,]

List[0]=17                                    #Changing the value at a given index by assigning new value to it
print(List)

print(List[2])                                # For checking the value at a certain index

print(List[1:3])                              # Forward slicing

print(List[-3:-1])                            # Backward slicing

print(len(List))                              # Tells the number of elements in a list

List.append(12)                               # Adds '12' at the end of the list
print(List)                                   

List.insert(3,51)                             # Adds '51' at the index value '3' of the list
print(List)

List.sort()                                   # Arranges the elements of the list in ascending order
print(List)

List.sort(reverse=True)                       # Arranges the elements of the list in descending order
print(List)

List.reverse()                                # Reverse the order of elements from the list
print(List)

List.remove(10)                               # Removes the element '10' from the list
print(List)

List.pop(2)                                   # Removes the element at index value '2'
print(List)

print(type(List))


##########
# TUPLES #
##########

Tup=('Number',17,32,26,17)

print(Tup[2])                                    # Tells element at index 2

print(Tup[1:3])                                  # Tells elements at index 1 and 2

print(Tup[-3:-1])                                # Tells elements at index -3 and -2

print(Tup.index(32))                             # Tells index value of 32

print(Tup.count(17))                             # Tells the number of times 17 occurs


################
# DICTIONARIES #
################

Dict={"Name":"Rohan",
      "subject":["Python", "Coding",11],
      "age":18,
      "topic":("dictionary","set",12),
      "another":{1:"R",2:"J"}}

print(Dict['age'])

Dict["Name"]="RJ"
print(Dict)

print(Dict.keys())                      # Returns list of keys

print(Dict.values())                    # Returns list of values

print(Dict.items())                     # prints (key,value) pairs in a list

print(Dict.get("Name"))                 # Returnd None if no such key exists

Dict.update({"City":"Delhi"})           # Adds another key:value pair


########
# SETS #
########

S={1,2,2,2,"Rohan",4.67}

print(len(S))                          # All same elements are converted into only one of them

S.add(5)                               # Adds an element in the set
print(S)

S.remove(2)                            # Removes an element from the set & raises error if element not found
print(S)

S.discard("Rohan")                     # Removes an element from the set & doesn't raise error if element not found
print(S)

S.pop()                                # Removes a random element from set  
print(S)

S.clear()                              # Empties the set
print(S)

S1={1,2,3,4}
S2={3,4,5,6,7}

print(S1.union(S2))                    # prints set of all elements in the set

print(S1.intersection(S2))             # prints common elements in the sets

#####################################################################################################################################################
#####################################################################################################################################################
def sum(a,b):                         # a and b are called parameters
    s=a+b
    A=print(s)
    return A                          # s is output
sum(6,9)                              # 6 and 9 are called arguements
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
def repeat(n):                        # Repeats element 'n' 'n+1' times 
    for I in range(n+1):
        print(n)
repeat(3)
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
def show(n):                          # Writes the numbers in descending order till 1 starting from n
    if (n==0):
        return
    print(n)
    show(n-1)
show(3)
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
def fact(n):
    if n<=1:                          # Prints the factorial of n
        return 1
    else:
        return fact(n-1)*n
print(fact(5))

####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

#####################
# FILE INPUT/OUTPUT #
#####################

# Opening a file
"""
<file_object>=open(<file_location/file_name>,<mode>)
with open(<file_location/file_name>,<mode>) as <file_object>:


<file_object> is called as <file_handle>

It basically acts as a variable to open a file.
"""

# Closing a file
"""
<file_handle>.close()

with open - opening statement - doesn't need any closing statement
"""

# Functions in a file
"""
TEXT FILES
read function - 'r'
write function - 'w'
append function - 'a'
read and write - 'r+'
write and read - 'w+'
append and read - 'a+'

BINARY FILES
read function - 'rb'
write function - 'wb'
append function - 'ab'
read and write - 'r+b' or 'rb+'
write and read - 'w+b' or 'wb+'
append and read - 'a+b' or 'ab+'

CSV FILES
read function - 'r'
write function - 'w'
append function - 'a'
"""

### TEXT FILES ###
"""
This is a type of file that can be directly read by the user.
It is written in ASCII and UNICODE characters.
"""

# Writing a file

"""
<file_object>=open(<file_location/file_name>,'w')         # 'w' is the symbol used to open the file in write mode

<file_handle>.write(<str>)                              # Writing a string <str> in a file referenced by <file_handle>
-------------or--------------
<file_handle>.writelines(<L>)                           # Writing all strings in a list <L> as lines to file referenced by <file_handle>

<file_handle>.close()

write function in a file totally erases all the pre-written words/set of characters in the file and then writes the string(s) assigned to the function.

A new file is created if file does not exist.
"""

# Reading a file

"""
<file_object>=open(<file_location/file_name>,'r')         # 'r' is the symbol used to open the file in read mode

<file_handle>.read(<n>)             # Reading n number of characters from a file referenced by <file_handle>.
-------------or--------------
<file_handle>.readline(<n>)         # Reading a line at a time from a file referenced by <file_handle>. If <n> is specified then atmost n number of characters from the line and then start the cursor from there onwards.
-------------or--------------
<file_handle>.readlines()           # Reading all lines from a file referenced by <file_handle> and returns them as a list.

<file_handle>.seek(<n>)            # Moves the cursor to nth byte in the file

<file_handle>.tell()               # Tells the position of the cursor

<file_handle>.close()

read function in a file prints the sets of characters from it according to the described funtion
read(<n>) statement reads the complete file if <n> is not specified
reading statements prints the lines according to the position of cursor.

Shows an error if file does not exist.
"""

# Appending a file

"""
<file_object>=open(<file_location/file_name>,'a')         # 'a' is the symbol used to open the file in append mode

<file_handle>.write(<str>)                             # Appending a string <str> in a file referenced by <file_handle>

<file_handle>.close()

A new file is created if file does not exist.
"""

# Writing in a file along with Reading it

"""
<file_handle> = open(<file_name>, 'w+')

<file_handle>.write(<str>)                              # Writing a string <str> in a file referenced by <file_handle>
-------------or--------------
<file_handle>.writelines(<L>)                           # Writing all strings in a list <L> as lines to file referenced by <file_handle>

<file_handle>.read(<n>)             # Reading n number of characters from a file referenced by <file_handle>
-------------or--------------
<file_handle>.readline(<n>)         # Reading a line at a time from a file referenced by <file_handle>. If <n> is specified then atmost n number of characters from the line 
-------------or--------------
<file_handle>.readlines()           # Reading all lines from a file referenced by <file_handle> and returns them as a list.

<file_handle>.seek(<n>)            # Moves the cursor to nth byte in the file

<file_handle>.tell()               # Tells the position of the cursor

<file_handle>.close()

A new file is created if file does not exist.
"""

# Reading in a file along with writing it

"""
<file_handle> = open(<file_name>, 'r+')

<file_handle>.read(<n>)             # Reading n number of characters from a file referenced by <file_handle>
-------------or--------------
<file_handle>.readline(<n>)         # Reading a line at a time from a file referenced by <file_handle>. If <n> is specified then atmost n number of characters from the line 
-------------or--------------
<file_handle>.readlines()           # Reading all lines from a file referenced by <file_handle> and returns them as a list.

<file_handle>.write(<str>)                              # Writing a string <str> in a file referenced by <file_handle>
-------------or--------------
<file_handle>.writelines(<L>)                           # Writing all strings in a list <L> as lines to file referenced by <file_handle>

<file_handle>.seek(<n>)            # Moves the cursor to nth byte in the file

<file_handle>.tell()               # Tells the position of the cursor

<file_handle>.close()

Shows an error if file does not exist.
"""

# Appending in a file along with Reading it

"""
<file_handle> = open(<file_name>, 'a+')

<file_handle>.write(<str>)                              # Writing a string <str> in a file referenced by <file_handle>

<file_handle>.read(<n>)             # Reading n number of characters from a file referenced by <file_handle>
-------------or--------------
<file_handle>.readline(<n>)         # Reading a line at a time from a file referenced by <file_handle>. If <n> is specified then atmost n number of characters from the line 
-------------or--------------
<file_handle>.readlines()           # Reading all lines from a file referenced by <file_handle> and returns them as a list.

<file_handle>.seek(<n>)            # Moves the cursor to nth byte in the file

<file_handle>.tell()               # Tells the position of the cursor

<file_handle>.close()

A new file is created if file does not exist.
"""

### BINARY FILES ###
"""
This is a type of file that can't be directly read by the user.
It is written in special characters.
"""
# Writing a file

"""
import pickle

<file_handle>=open(<file_location/file_name>,'wb')         # 'wb' is the symbol used to open the file in write mode

pickle.dump(<str>,<file_handle>)

<file_handle>.close()
"""

# Reading a file

"""
import pickle

<file_object>=open(<file_location/file_name>,'rb')         # 'rb' is the symbol used to open the file in read mode

pickle.load(<file_handle>)

<file_handle>.close()
"""

# Appending a file

"""
import pickle

<file_object>=open(<file_location/file_name>,'ab')         # 'ab' is the symbol used to open the file in append mode

pickle.dump(<str>,<file_handle>)

<file_handle>.close()
"""

### C.S.V. FILES ###
"""
This type of file is used for tabular data. 
The values of tabular sructure is seperated using commas (delimiter).
"""

# Reading a file

"""
import csv

<file_handle>=open(<file_name>,'r')

<reader_object>=csv.reader(<file_name>,delimiter=',')

<list_object>=list(<reader_handle>)

print(<list_Object>)

<file_handle>.close()

Prints a row as a list and the total text as a list with multiple different lists(different rows) in it.
Can also be done as tuples as well.
',' is acting as delimiter.
"""

# Writing a file

"""
import csv

<file_handle>=open(<file_name>,'w')

<writer_object>=csv.writer(<file_name>,delimiter=',')

<writer_object>.writerow([<a>,<b>,<c>,<d>])
<writer_object>.writerow([<e>,<f>,<g>,<h>])
<writer_object>.writerow([<i>,<j>,<k>,<l>])
-------------------or----------------------
<list_object>=[[<a>,<b>,<c>,<d>],[<e>,<f>,<g>,<h>][<i>,<j>,<k>,<l>]]
<writer_object>.writerows(<list_object>)

<file_handle>.close()

Writes a row as text seperated by ','
Can also be done as tuples as well.
',' is acting as delimiter.
"""

"""
GO TO "FILE HANDLING" File FOR THE EXAMPLES FOR ABOVE TOPIC - ' Functions in a file '.
"""

###################################################################################################################################################
###################################################################################################################################################
###################################################################################################################################################

###########
# MODULES #
###########
"""
1.  math module
2.  cmath module
3.  random module
4.  statistics module
5.  pickle module                              - <<< Shown above >>> -
6.  csv module                                 - <<< Shown above >>> -
"""

"""
GO TO "MODULE" File FOR THE FUNCTIONS AND EXAMPLES FOR ABOVE TOPIC - ' Modules '.

"""

######################################################################+====+#######################################################################
######################################################################|OOPS|#######################################################################
######################################################################+====+#######################################################################

########################
# REGULAR  EXPRESSIONS #
########################

import re

# 1. match(What_To_Find, From_Where_To_Search)                            # Checks a definite number letters and tells if they match of not

a = "ABCD"
if re.match(a,"ABCD"):                                                    # Will return true if first 4 letters of 'string' and 'a' are same
    print("True 1")
else:
    print("False 1")

if re.match(a,"ABC"):
    print("True 2")
else:
    print("False 2")

if re.match(a,"ABCDEFGH"):
    print("True 3")
else:
    print("False 3")

if re.match(a,"EABCD"):
    print("True 4")
else:
    print("False 4")

# 2. findall(What_To_Find, From_Where_To_Search, flags)

a = "ABCD"
print(re.findall("ABCD",a))

text = "My phone number is 9876543210 and office is 0123456789"
numbers = re.findall(r'\d+', text)                                        # \d+ means 'numbers' only
print(numbers)

text = "Python is fun and powerful!"
words = re.findall(r'\w+', text)                                          # \w+ means 'words' only
print(words)

text = "Python is Amazing. PYTHON is versatile."
matches = re.findall(r'python', text, re.IGNORECASE)
print(matches)

text = "Email: abc@example.com and xyz@test.com"
emails = re.findall(r"\w+@\w+\.\w+", text)
print(emails)


# 3. search(What_To_Find, From_Where_To_Search, flags)

text = "Welcome to Python programming"
result = re.search("program", text)                                       # Unlike match which checks only first 4 letters, it searches the entirety of string
if result:
    print("Found:", result.group())
else:
    print("Not found")

text = "ID: 5678"
result = re.search(r"\d+", text)
print("Found:", result.group())

# fullmatch(pattern, string, flags)

print(re.fullmatch(r"\d+", "12345"))                                      # full match (digits only)
print(re.fullmatch(r"\d+", "123abc"))                                     # not a full match

# sub(pattern, replacement, string, count=0, flags=0)

text = "I love Python. Python is great."
result = re.sub(r"Python", "Java", text)
print(result)

text = "apple, apple, apple"
result = re.sub(r"apple", "orange", text, count=2)
print(result)

text = "My ID is 12345 and PIN is 6789"
result = re.sub(r"\d", "", text)
print(result)

text = "Too     many    spaces"
result = re.sub(r"\s+", " ", text)                                        # Replaces extra spaces
print(result)

# Characters and character sequences

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Matches any one of a, b, or c
print(re.findall(r"[abc]", "apple banana cherry"))

# Matches any lowercase letter
print(re.findall(r"[a-z]", "ABCdef123"))

# Matches any uppercase letter
print(re.findall(r"[A-Z]", "AbCdEf"))

# Matches any digit from 0 to 9
print(re.findall(r"[0-9]", "Room 123"))

# Matches any character except a, b, or c
print(re.findall(r"[^abc]", "abcxyz"))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# \d matches any digit
print(re.findall(r"\d", "Phone: 123-456"))

# \D matches any non-digit character
print(re.findall(r"\D", "Phone: 123-456"))

# \w matches any alphanumeric character or underscore
print(re.findall(r"\w", "Hi_123!"))

# \W matches any non-alphanumeric character
print(re.findall(r"\W", "Hi_123!"))

# \s matches any whitespace character (space, tab, newline)
print(re.findall(r"\s", "New York\nCity"))

# \S matches any non-whitespace character
print(re.findall(r"\S", "New York"))

# \b matches word boundaries
print(re.findall(r"\bcat", "cat scatter catalog"))

# \B matches positions that are not word boundaries
print(re.findall(r"\Bcat", "cat scatter catalog"))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# * matches 0 or more of the preceding expression
print(re.findall(r"ab*", "a ab abb abbb"))

# + matches 1 or more of the preceding expression
print(re.findall(r"ab+", "a ab abb abbb"))

# ? matches 0 or 1 of the preceding expression
print(re.findall(r"ab?", "a ab abb abbb"))

# {2} matches exactly 2 repetitions of 'a'
print(re.findall(r"a{2}", "aa aaa aaaa"))

# {2,} matches 2 or more repetitions of 'a'
print(re.findall(r"a{2,}", "aa aaa aaaa"))

# {2,3} matches between 2 and 3 repetitions of 'a'
print(re.findall(r"a{2,3}", "aa aaa aaaa"))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# ^ matches the start of a string
print(re.findall(r"^Hello", "Hello World"))

# $ matches the end of a string
print(re.findall(r"World$", "Hello World"))

# 5. Groups and Alternation

# (ha)+ matches one or more repetitions of 'ha'
print(re.findall(r"(ha)+", "hahaha"))

# cat|dog matches either 'cat' or 'dog'
print(re.findall(r"cat|dog", "I love my cat and dog"))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Escaping '.' which is otherwise a wildcard
print(re.findall(r"\.", "price is 10.99"))

# Escaping '$' which has special meaning in regex
print(re.findall(r"\$", "Cost is $5"))

# Escaping brackets to match literal [test]
print(re.findall(r"\[test\]", "Check [test]"))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

sample_text = "My ID is A123, and I paid $20.50 for 3 items on 2025-07-09."

# Matches an uppercase letter followed by digits (like an ID)
print(re.findall(r"[A-Z]\d+", sample_text))         # ['A123']

# Matches floating point numbers
print(re.findall(r"\d+\.\d+", sample_text))         # ['20.50']

# Matches date format YYYY-MM-DD
print(re.findall(r"\d{4}-\d{2}-\d{2}", sample_text)) # ['2025-07-09']
