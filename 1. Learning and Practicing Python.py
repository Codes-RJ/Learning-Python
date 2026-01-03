
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

print(ord('a'))                          # Tells the ASCII value of character 'a'

print(chr(97))                         # Tells the character of ASCII value 97


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


print(max(4,7,2,9,1))                  # Gives maximum number from the given numbers
print(min(4,7,2,9,1))                  # Gives minimum number from the given numbers
print(abs(-56))                        # Gives absolute value of the number
print(pow(3,4))                        # Gives 3 raised to power 4

a=round(6.4+9.45)                      # Gives round integer data type figure of 'a'
print(a)                               # A number x.5 will return x+1


##########################
# if-elif-else statement #
##########################

# Block Structure

"""
if (Condition1):
      "Statement1"
elif (Condition2):
      "Statement2"
else:
      "Statement3"

Which statement will execute depends on which condition is met by the  variable or something
"""

# Short Hand if-else --or-- Ternary Operator
"""
"Statement1" if (Condition1) else "Statement" if (Condition2) else "Statement3 "
"""


#############
# For Loops #
#############

# Structure
"""
for <variable> in <iterable>:
    (Code Block)
"""
# Example
for i in range(5):                 # Prints numbers from 0 to 4
    print(i)

for i in range(1,6):               # Prints numbers from 1 to 5
    print(i)

for i in range(1,11,2):            # Prints numbers from 1 to 10 at an interval of 2
    print(i)

for i in range(10, 0, -1):         # Prints numbers from 10 to 1 in descending order
    print(i)

for i in "Python":                 # Prints each character of the string 'Python' in a new line
    print(i)

for i in [2,4,6,8,10]:             # Prints each element of the list in a new line
    print(i)

numbers = [10, 20, 30]
for i in range(len(numbers)):      # Prints each element of the list in a new line
    print(numbers[i])

for i in range(1, 4):              # Nested for loop
    for j in range(1, 4):
        print(i, j)

for el in List:                    # Printing the elements in a list
    print(el)
else:                              # Executes after the loop is over
    print('Over')


###############
# While Loops #
###############

# Structure
"""
while (Condition):
    (Code Block)
"""

# Example
i=1
while i<=5:                      # Prints numbers from 1 to 5
    print(i)
    i+=1

while False:                  # Does not print anything as condition is false
    print("Hello")

while True:                   # Prints 'Hello' infinite times as condition is true
    print("Hello")

while True:
    print("Hello")
    break                      # Breaks the infinite loop

while True:
    print("Hello")
    continue                   # Continues the infinite loop

while True:
    print("Hello")
    pass                       # Does nothing and continues the infinite loop

i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1


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


###########
# Strings #
###########
"""Immutable Data Type"""

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

print(str.count('si'))                     # Counts the number of times 'si' occurs in the string 

S1="NEGATIVE"                              # N  E  G  A  T  I  V  E
print(S1[-6:-2])                           #-8 -7 -6 -5 -4 -3 -2 -1

name="           Virat Kolhi Sir              "
print(name.strip())                        # Replaces the space from start and end of the string

name="virat kolhi sir"
print(name.title())                        # Capitalizes the first letter of every word of the string

print(name.upper())                        # Converts the whole string to upper case letters

print(name.lower())                        # Converts the whole string to lower case letters

print(name.swapcase())                     # Converts upper case letters to lower case letters and vice versa

print(name.isalpha())                      # Checks if all characters in the string are alphabets (no spaces or numbers)

print(name.isalnum())                      # Checks if all characters in the string are alphanumeric (no spaces)

print(name.islower())                      # Checks if all characters in the string are in lower case

print(name.isupper())                      # Checks if all characters in the string are in upper case

print(name.isspace())                      # Checks if all characters in the string are spaces

print(name.index('k'))                     # Tells the index value of first occurence of 'k' in the string

print(name.find('k'))                      # Tells the index value of first occurence of 'k' in the string

print(name.replace('kolhi', 'kohli'))      # Replaces the first presence of 'kolhi' to 'kohli'

print(name.startswith('v'))                # Checks if the string starts with a particular letter/Character/set of them

print(name.endswith('r'))                  # Checks if the string ends with a particular letter/Character/set of them

print('i' in name)                         # Checks if 'i' is present in the string and returns True or False

print('z' not in name)                     # Checks if 'z' is not present in the string and returns True or False

print(name.split(' '))                     # Splits the string from the given character and returns a list of strings

print("Point"=="point")                    # Compares 2 strings and returns True if both are same else returns False


#########
# LISTS #
#########
"""Mutable Data Type"""

List=['Senenteen',10,2.4,76]

print(List)

print(type(List))

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

print(sorted(List))                            # Tells the sorted list in ascending order without changing the original list

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

list2=List.copy()                             # Copies the list to another list
print(list2)

list2.clear()                                 # Empties the list
print(list2)

list=[1,2,3,4,2,5,2,6]
print(list)

List+=list                                    # Extends the list by adding another list at the end of it
print(List)

List.extend(list)                             # Extends the list by adding another list at the end of it
print(List)

print(List.count(2))                          # Tells the number of times 2 occurs in the list

print(3 in List)                              # Checks if 3 is present in the list and returns True or False

print(9 not in List)                          # Checks if 9 is not present in the list and returns True or False

print(max(List))                               # Tells the maximum element from the list

print(min(List))                               # Tells the minimum element from the list

print(sum(List))                               # Tells the sum of all elements from the list

L=[[[3,6],[2,8]],[4,1],[9,5],7]                # Nested List

print(L[2][1])                                 # Tells element at index 1 of list at index 2

print(L[0][1][0])                              # Tells element at index 0 of list at index 1 of list at index 0

print(L[-2][-1])                               # Tells element at index -1 of list at index -2


##########
# TUPLES #
##########
"""Immutable Data Type"""

Tup=('Number',17,32,26,17)

print(Tup)

print(type(Tup))

print(Tup[2])                                    # Tells element at index 2

print(Tup[1:3])                                  # Tells elements at index 1 and 2

print(Tup[-3:-1])                                # Tells elements at index -3 and -2

print(Tup.index(32))                             # Tells index value of 32

print(Tup.count(17))                             # Tells the number of times 17 occurs

Tup2=('Rohan',18)

Tup3=Tup+Tup2                                    # Concatenation of 2 tuples
print(Tup3)

print(len(Tup3))                                 # Tells the number of elements in the tuple

print(max(Tup3))                                 # Tells the maximum element from the tuple

print(min(Tup3))                                 # Tells the minimum element from the tuple

print(sum((17,32,26,17)))                        # Tells the sum of all elements from the tuple

print(sorted(Tup3))                              # Tells the sorted tuple in ascending order without changing the original tuple

print(Tup.sorted())                              # Tells the sorted tuple in ascending order without changing the original tuple

print(Tup.sorted(reverse=True))                  # Tells the sorted tuple in descending order without changing the original tuple

#Tup.sort()                                      # ERROR because tuples are immutable

print(tuple(List))                               # Converts a list into a tuple

print(18 in Tup3)

print(20 not in Tup3)


################
# DICTIONARIES #
################
"""Key : Immutable Data Type , Value : Mutable Data Type"""

Dict={"Name":"Rohan",
      "subject":["Python", "Coding",11],
      "age":18,
      "topic":("dictionary","set",12),
      "another":{1:"R",2:"J"}}

print(Dict)                                 # Prints the entire dictionary

print(Dict['age'])

Dict["Name"]="RJ"                           # Changing the value of a given key by assigning new value to it
print(Dict)

Dict['grade']='A'                           # Adding another key:value pair
print(Dict)

print(Dict.keys())                          # Returns list of keys

print(Dict.values())                        # Returns list of values

print(Dict.items())                         # prints (key,value) pairs in a list

print(Dict.get("Name"))                     # Returns None if no such key exists instead of throwing an error else gives value of the key

print(Dict.get("Names","Not Found"))        # Returns the default value provided if no such key exists

print(Dict.setdefault("Name","Default"))    # Returns value of the key if it exists else adds the key with the default value provided

print(Dict.pop("age"))                      # Removes the key:value pair and returns the value of the key

Dict.update({"City":"Delhi"})               # Adds another key:value pair
print(Dict)

print(Dict.popitem())                       # Removes the last inserted key:value pair and returns it as a tuple

print("Name" in Dict)

print("age" not in Dict)

print(len(Dict))                            # Returns number of key:value pairs in the dictionary

print(type(Dict))                           # Returns the type of the data structure

print(isinstance(Dict,dict))                # Returns True if the data structure is of the given type else returns False

print(Dict.copy())                          # Returns a shallow copy of the dictionary

print("RJ" in Dict)

print("Delhi" not in Dict)

print("RJ" in Dict.values())

print(Dict.clear())                         # Removes all key:value pairs from the dictionary

print(Dict.fromkeys(["a","b","c"],0))       # Creates a new dictionary with the given keys and assigns them the given default value


########
# SETS #
########
"""Mutable Data Type"""

S={1,2,2,2,"Rohan",4.67}               # Sets are unordered & unindexed collections of unique elements

print(S)                               # All same elements are converted into only one of them

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

Sn = S1 | S2                           # Union of S1 and S2 (More the | symbol, more the sets can be unioned)
print(Sn)

print(S1.intersection(S2))             # prints common elements in the sets

Sn = S1 & S2                           # Intersection of S1 and S2 (More the & symbol, more the sets can be intersected)

print(S1.difference(S2))               # prints elements in S1 but not in S2

Sn = S1 - S2                           # Difference of S1 and S2 (More the - symbol, more the sets can be differenced)
print(Sn)

print(S1.symmetric_difference(S2))     # prints elements in S1 and S2 but not in both

print(S1.issubset(S2))                 # checks if S1 is subset of S2

print(S1.issuperset(S2))               # checks if S1 is superset of S2

print(S1.isdisjoint(S2))               # checks if S1 and S2 have no elements in common

print(2 in S1)                         # checks if 2 is present in S1

print(9 not in S2)                     # checks if 9 is not present in S2

#S3 = S1 + S2                          # ERROR because sets do not support concatenation

S3 = S1.copy()                         # Copies S1 to S3
print(S3)

S4 = S3.update({8,9})                  # Adds elements 8 and 9 to S3
print(S4)


###############
# FROZEN SETS #
###############
"""Immutable Data Type"""

FS=frozenset({1,2,3,4,5})

print(FS)

print(type(FS))

#print(FS.add(6))                      # ERROR because frozensets are immutable

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

.... etc

"""

"""
GO TO "MODULE" File FOR THE FUNCTIONS AND EXAMPLES FOR ABOVE TOPIC - ' Modules '.

"""

######################################################################+====+#######################################################################
######################################################################|OOPS|#######################################################################
######################################################################+====+#######################################################################


