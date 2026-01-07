
# ---+---  +---+  \   /  ---+---     +---+  --+--  |     +---+  +---+
#    |     |       \ /      |        |        |    |     |      |
#    |     +---+    +       |        +--+     |    |     +--+   +---+
#    |     |       / \      |        |        |    |     |          |
#    |     +---+  /   \     |        |      --+--  +---- +---+  +---+

str="Hi. My name is Rohan. I am learning Python."

str2="\nIt's super easy to use."

L=["Hi.", "My name is Rohan.", "I am learning Python."]

L2=["Hi.\n", "My name is Rohan.\n", "I am learning Python."]

######################################
# write (w), read (r) and append (a) #
######################################

f=open('File 1.txt','w')
f.write(str)
f.close()

f=open('File 2.txt','w')
f.writelines(L)
f.close()

f=open('File 3.txt','w')
f.writelines(L2)
f.close()

f=open('File 1.txt','r')
print(f.read())
f.close()

f=open('File 1.txt','r')
print(f.read(17))
f.close()

f=open('File 3.txt','r')
print(f.readline())
f.close()

f=open('File 3.txt','r')
print(f.readline(2))
print(f.readline())
f.close()

f=open('File 3.txt','r')
print(f.readlines())
f.close()

f=open('File 3.txt','a')
f.write(str2)
f.close()

"""
w mode is used to write in the file while removing any previous data in it. If no file exist, a new file is created.
r mode is used to read from the file. If no file exist, error occurs.
a mode is used to write in the file while keeping any previous data in it. If no file exist, a new file is created.
"""
"""
read(size)            :   Reads the file content as a single string; whole file if size is omitted, otherwise up to size characters.
readline(size)        :   Reads one line as a string; if size is given, reads at most size characters from that line.
readlines(sizehint)   :   Reads all remaining lines and returns a list of strings; sizehint roughly limits total bytes read.
write(string)         :   Writes the given string to the file and returns the number of characters written (no automatic newline).
writelines(iterable)  :   Writes each string from the iterable to the file exactly as given, without adding newlines automatically
"""

#######################
# The with statements #
#######################

# Instead of using :-
f = open('File 1.txt', 'r')
data = f.read()
f.close()

# Prefer
with open('File 1.txt', 'r') as f:
    data = f.read()

""" This avoids forgetting close() and makes code cleaner. """

####################
# Combo Operations #
####################
# First create a file normally
with open("demo_r_plus.txt", "w") as f:
    f.write("Hello Rohan\nSecond line\n")

# r+ mode (read + write, no truncation)
with open("demo_r_plus.txt", "r+") as f:
    print("Initial content:")
    print(f.read())                               # read existing data
    f.seek(0)                                     # move pointer to start
    f.write("Hi")                                 # overwrite first 2 characters
"""
- If "demo_r_plus.txt" does not exist, opening with 'r+' raises an error, because the file must already exist.
- Writing overwrites from the current pointer position, it does not auto-append.
"""

# If file exists, its content will be cleared
with open("demo_w_plus.txt", "w+") as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.seek(0)                                     # go back to beginning to read
    print("Content in w+ file:")
    print(f.read())
"""
If "demo_w_plus.txt" exists, its previous content is deleted immediately when opened with 'w+'.
If it does not exist, 'w+' creates a new file and allows both reading and writing.
"""

# Create or open file in append+read mode
with open("demo_a_plus.txt", "a+") as f:
    f.write("New line added\n")                   # always written at end
    # To read from beginning, move pointer to start
    f.seek(0)
    print("Content in a+ file:")
    print(f.read())
"""
If "demo_a_plus.txt" does not exist, 'a+' creates it.
Writes always go to the end of the file, even if you used seek() before writing.
"""

#################
# File Pointers #
#################

with open("sample.txt", "r") as f:
    print("Position at start:", f.tell())         # usually 0
    data = f.read(5)                              # read 5 characters
    print("Read:", data)
    print("Position after read(5):", f.tell())
"""
tell() returns the current byte position from the beginning of the file.
After reading some characters, the returned position increases accordingly.
"""

with open("sample.txt", "r") as f:
    f.seek(0)                                     # go to start
    print("At start:", f.tell())
    f.seek(10)                                    # move to 10th byte from beginning
    print("At 10:", f.tell())
    # read from position 10
    print("From 10:", f.read(5))
"""
Default whence is 0, meaning “from beginning of file”, so f.seek(n) means “go to position n from start”.
"""

with open("sample.txt", "rb") as f:
    # from beginning (whence = 0)
    f.seek(5, 0)
    # from current position (whence = 1)
    f.seek(3, 1)                                  # move 3 bytes forward from current position
    # from end (whence = 2), typically with negative offset
    f.seek(-5, 2)                                 # go to 5 bytes before end
    print("Position near end:", f.tell())
"""
whence = 0: from beginning, whence = 1: from current position, whence = 2: from end (commonly used with negative offsets).
"""


###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################

# +---+  --+--  |   |  +---+  +---+  |   |    +---+ --+--  |      +---+  +---+
# |   |    |    |\  |  |   |  |   |   \ /     |       |    |      |      |
# +--+     |    | \ |  |---+  +---+    +      +---+   |    |      +--+   +---+
# |   |    |    |  \|  |   |  |\       |      |       |    |      |          |
# +---+  --+--  |   |  |   |  | \      |      |     --+--  +---+  +---+  +---+

import pickle

################################################
# Binary read (rb), write (wb) and append (ab) #
################################################

import pickle  # using pickle to store Python objects in a binary file

str  = "Hi. My name is Rohan. I am learning Python."
str2 = "\nIt's super easy to use."
L    = ["Hi.", "My name is Rohan.", "I am learning Python."]
L2   = ["Hi.\n", "My name is Rohan.\n", "I am learning Python."]

# ---------- WRITE (wb) ----------
with open("Binary_multi", "wb") as f:               # file is created/cleared, ready to store objects
    pickle.dump(str,  f)                            # "Hi. My name is Rohan. I am learning Python."
    pickle.dump(str2, f)                            # "Hi. My name is Rohan. I am learning Python."  +  "\nIt's super easy to use."
    pickle.dump(L,   f)                             # above 2 strings  +  ["Hi.", "My name is Rohan.", "I am learning Python."]
    pickle.dump(L2,  f)                             # all above 3 objects  +  ["Hi.\n", "My name is Rohan.\n", "I am learning Python."]

# ---------- READ (rb) ----------
with open("Binary_multi", "rb") as f:               # open same file to read objects in order
    s1 = pickle.load(f)                             # s1 = "Hi. My name is Rohan. I am learning Python."
    s2 = pickle.load(f)                             # s2 = "\nIt's super easy to use."
    l1 = pickle.load(f)                             # l1 = ["Hi.", "My name is Rohan.", "I am learning Python."]
    l2 = pickle.load(f)                             # l2 = ["Hi.\n", "My name is Rohan.\n", "I am learning Python."]

# ---------- APPEND (ab) ----------
data1 = "First"                                     # 5th object value

with open("Binary_multi", "ab") as f:               # open file in append mode (do not erase old data)
    pickle.dump(data1, f)                           # file now has all 4 previous objects + "First" at the end

# ---------- READ ALL 5 OBJECTS ----------
with open("Binary_multi", "rb") as f:               # read again to see all objects including appended one
    s1  = pickle.load(f)                            # "Hi. My name is Rohan. I am learning Python."
    s2  = pickle.load(f)                            # "\nIt's super easy to use."
    l1  = pickle.load(f)                            # ["Hi.", "My name is Rohan.", "I am learning Python."]
    l2  = pickle.load(f)                            # ["Hi.\n", "My name is Rohan.\n", "I am learning Python."]
    d1  = pickle.load(f)                            # "First"

# When do we actually use binary files ?
data = {"name": "Rohan", "age": 20}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)                          # store dict as binary

#####################
# Seek() and Tell() #
#####################

with open("data.pkl", "rb") as f:
    obj = pickle.load(f)                          # get back dict
print(obj)

with open("raw.bin", "wb") as f:
    f.write(b"ABCDEFGH")                          # 8 bytes

with open("raw.bin", "rb") as f:
    print(f.tell())                               # 0
    f.seek(3)                                     # go to 4th byte
    print(f.read(2))                              # b"DE"
    print(f.tell())                               # 5


###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################

# +---+   +---+   \        /     +---+  --+--  |      +---+  +---+
# |       |        \      /      |        |    |      |      |
# |     O +---+ O   \    /  O    +--+     |    |      +--+   +---+
# |           |      \  /        |        |    |      |          |
# +---+   +---+       \/         |      --+--  +----  +---+  +---+

import CSV

# ---------- WRITE csv 1 ----------
f = open('csv 1', 'w', newline='')          # open for writing text; existing content (if any) is cleared
writer = csv.writer(f, delimiter=',')       # writer will write each list as one CSV row, columns separated by commas
writer.writerow([1, 2, 3, 4])               # line 1 ->  1,2,3,4
writer.writerow([5, 6, 7, 8])               # line 2 ->  5,6,7,8
writer.writerow(['a', 'b', 'c', 'd'])       # line 3 ->  a,b,c,d
f.close()

# ---------- WRITE csv 2 ----------
f = open('csv 2', 'w', newline='')
writer = csv.writer(f, delimiter=',')       # same writer, comma-separated
L = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     ['a', 'b', 'c', 'd']]                  # list of rows; each inner list will become one CSV row
writer.writerows(L)  
"""
writes all 3 rows:
line 1 -> 1,2,3,4
line 2 -> 5,6,7,8
line 3 -> a,b,c,d
"""
f.close()

# ---------- READ csv 1 ----------
f = open('csv 1', 'r', newline='')         # open for reading text
read = csv.reader(f, delimiter=',')        # csv.reader reads each row and splits by comma; each row becomes a list of strings
L = list(read)                             
"""
consume all rows into a Python list:
L = [
  ['1', '2', '3', '4'],
  ['5', '6', '7', '8'],
  ['a', 'b', 'c', 'd']
]
"""
print(L)
f.close()

# ---------- READ csv 2 ----------
f = open('csv 2', 'r', newline='')   # open for reading text
read = csv.reader(f, delimiter=',')  # same as above
L = list(read)  
"""
again:
L = [
  ['1', '2', '3', '4'],
  ['5', '6', '7', '8'],
  ['a', 'b', 'c', 'd']
]
"""
print(L)
f.close()

"""
writer.writerow(list) → writes one row to the CSV file; each element is one column.
writer.writerows(list_of_lists) → writes multiple rows, one for each inner list.
csv.reader(file) → reads each CSV line and returns rows as lists of strings.
"""

# Writing through a Dictionary in CSV File
with open("file.csv", "w", newline="") as f:
    fieldnames = ["roll", "name", "marks"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"roll": 1, "name": "Rohan", "marks": 95})
"""
roll | name  | marks
-----+-------+------
1    | Rohan | 95
"""

############################################################################
############################################################################
############################################################################
############################################################################
# DONE                                                                DONE #
#                                   DONE                                   #
# DONE                                                                DONE #
############################################################################
############################################################################
############################################################################
############################################################################

