##################
# Basic Programs #
##################

#---------------------------------#
# Pattern printing using for loop #
#---------------------------------#

"""
*
**
***
****
*****
"""
for i in range(1, 6):
    print("*" * i)


"""
*****
****
***
**
*
"""
for i in range(5, 0, -1):
    print("*" * i)


"""
    *
   **
  ***
 ****
*****
"""
for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)


"""
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)


"""
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
"""
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)
for i in range(4, 0, -1):
    print(" " * (5 - i) + "* " * i)


"""
*
* *
*   *
*     *
* * * * *
"""
for i in range(1, 6):
    if i == 1 or i == 5:
        print("*" * i)
    else:
        print("*" + " " * (i - 2) + "*")


"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
for i in range(5):
    print("* " * 5)


"""
* * * * *
*       *
*       *
*       *
* * * * *
"""
for i in range(1, 6):
    if i == 1 or i == 5:
        print("* " * 5)
    else:
        print("*" + " " * 7 + "*")


"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()


"""
1
2 3
4 5 6
7 8 9 10
"""
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


"""
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
"""
n = 5
for i in range(n):
    print(" " * (n - i), end="")
    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()


"""
     1
    1 1
   1 2 1
  1 2 2 1
 1 2 3 2 1
"""
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        if j <= (i + 1) // 2:
            print(j, end=" ")
        else:
            print(i - j + 1, end=" ")
    print()


#-----------#
# Factorial #
#-----------#

n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)


n = 5
fact = 1
while n > 0:
    fact *= n
    n -= 1
print("Factorial =", fact)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print("Factorial =", factorial(5))


#--------------------------#
# Count digits of a number #
#--------------------------#

n = int(input("Enter number: "))
# Handle negative number
if n < 0:
    n = -n
# Handle zero case
if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        count += 1
        n //= 10
print("Number of digits =", count)


n = int(input("Enter number: "))
# Handle negative number
n = abs(n)
count = 0
for digit in str(n):
    count += 1
print("Number of digits =", count)


#------------------------#
# Reverse a given number #
#------------------------#

n = int(input("Enter number: "))
# Handle negative number
is_negative = n < 0
n = abs(n)
reversed_num = 0
while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n //= 10
if is_negative:
    reversed_num = -reversed_num
print("Reversed number =", reversed_num)              # Will remove 0 at the end (e.g., 120 -> 21)


n = int(input("Enter number: "))
# Handle negative number
is_negative = n < 0
n = abs(n)
reversed_num = ''.join(reversed(str(n)))
if is_negative:
    reversed_num = '-' + reversed_num
print("Reversed number =", reversed_num)              # Will keep 0 at the end (e.g., 120 -> 021)


#---------------#
# Sum of digits #
#---------------#

n = int(input("Enter number: "))
# Handle negative number
n = abs(n)
sum_of_digits = 0
while n > 0:
    digit = n % 10
    sum_of_digits += digit
    n //= 10
print("Sum of digits =", sum_of_digits)


n = int(input("Enter number: "))
# Handle negative number
n = abs(n)
sum_of_digits = sum(int(digit) for digit in str(n))
print("Sum of digits =", sum_of_digits)


#------------------#
# Palindrome check #
#------------------#

n = int(input("Enter number: "))
# Handle negative number
is_negative = n < 0
n = abs(n)
reversed_num = 0
temp = n
while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n //= 10
if is_negative:
    reversed_num = -reversed_num
if temp == abs(reversed_num):
    print("Palindrome")
else:
    print("Not a palindrome")


n = int(input("Enter number: "))
# Handle negative number
is_negative = n < 0
n = abs(n)
reversed_num = ''.join(reversed(str(n)))
if is_negative:
    reversed_num = '-' + reversed_num
if str(n) == reversed_num:
    print("Palindrome")
else:
    print("Not a palindrome")


#-----------------#
# Armstrong check #
#-----------------#

n = int(input("Enter number: "))
# Handle negative number
is_negative = n < 0
n = abs(n)
num_digits = len(str(n))
sum_of_powers = 0
temp = n
while n > 0:
    digit = n % 10
    sum_of_powers += digit ** num_digits
    n //= 10
if is_negative:
    sum_of_powers = -sum_of_powers
if temp == abs(sum_of_powers):
    print("Armstrong number")
else:
    print("Not an Armstrong number")


n = int(input("Enter number: "))
# Handle negative number
is_negative = n < 0
n = abs(n)
num_digits = len(str(n))
sum_of_powers = sum(int(digit) ** num_digits for digit in str(n))
if is_negative:
    sum_of_powers = -sum_of_powers
if temp == abs(sum_of_powers):
    print("Armstrong number")
else:
    print("Not an Armstrong number")


#------------------#
# Fibonacci series #
#------------------#

n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


n = 10
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib_series = [0, 1]
    for _ in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

print(fibonacci(10))


#-------------------------------#
# Deleting keys from Dictionary #
#-------------------------------#

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Delete key 'b'
if 'b' in my_dict:
    del my_dict['b']
print(my_dict)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Delete key 'b' using pop
removed_value = my_dict.pop('b', None)
print(my_dict)
print("Removed value:", removed_value)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Delete key 'b' and 'c' using pop with a loop
for key in ['b', 'c']:
    my_dict.pop(key, None)                               # Using None to avoid KeyError if key not found
print(my_dict)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Delete key 'b' using popitem (removes last inserted item)
removed_item = my_dict.popitem()                         # Note: popitem removes the last item, not a specific key
print(my_dict)
print("Removed item:", removed_item)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Clear the entire dictionary
my_dict.clear()
print(my_dict)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Delete the entire dictionary
del my_dict
# print(my_dict)                                         # This will raise an error since my_dict is deleted
