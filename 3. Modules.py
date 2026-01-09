# |\  /|  +---+  --+--  |   |
# | \/ |  |   |    |    |   |
# |    |  +---+    |    |---|
# |    |  |   |    |    |   |
# |    |  |   |    |    |   |


# math.ceil(x): Returns the smallest integer greater than or equal to ( x ).
# Python

import math
print(math.ceil(4.3))  # Output: 5

# math.floor(x): Returns the largest integer less than or equal to ( x ).
# Python

import math
print(math.floor(4.7))  # Output: 4

# math.fabs(x): Returns the absolute value of ( x ).
# Python

import math
print(math.fabs(-5.5))  # Output: 5.5

# math.exp(x): Returns ( e^x ).
# Python

import math
print(math.exp(2))  # Output: 7.3890560989306495

# math.log(x[, base]): Returns the logarithm of ( x ) to the given base.
# Python

import math
print(math.log(8, 2))  # Output: 3.0

# math.sqrt(x): Returns the square root of ( x ).
# Python

import math
print(math.sqrt(16))  # Output: 4.0

# math.sin(x): Returns the sine of ( x ) (x in radians).
# Python

import math
print(math.sin(math.pi / 2))  # Output: 1.0

# math.cos(x): Returns the cosine of ( x ) (x in radians).
# Python

import math
print(math.cos(0))  # Output: 1.0

# math.tan(x): Returns the tangent of ( x ) (x in radians).
# Python

import math
print(math.tan(math.pi / 4))  # Output: 1.0

# math.degrees(x): Converts angle ( x ) from radians to degrees.
# Python

import math
print(math.degrees(math.pi))  # Output: 180.0

# math.radians(x): Converts angle ( x ) from degrees to radians.
# Python

import math
print(math.radians(180))  # Output: 3.141592653589793

# math.sinh(x): Returns the hyperbolic sine of ( x ).
# Python

import math
print(math.sinh(1))  # Output: 1.1752011936438014

# math.cosh(x): Returns the hyperbolic cosine of ( x ).
# Python

import math
print(math.cosh(1))  # Output: 1.5430806348152437

# math.tanh(x): Returns the hyperbolic tangent of ( x ).
# Python

import math
print(math.tanh(1))  # Output: 0.7615941559557649

# math.factorial(x): Returns the factorial of ( x ).
# Python

import math
print(math.factorial(5))  # Output: 120

# math.gcd(x, y): Returns the greatest common divisor of ( x ) and ( y ).
# Python

import math
print(math.gcd(48, 18))  # Output: 6

# math.comb(n, k): Returns the number of ways to choose ( k ) items from ( n ) items without repetition and without order.
# Python

import math
print(math.comb(5, 2))  # Output: 10

# math.copysign(x, y): Returns a float with the magnitude of ( x ) but the sign of ( y ).
# Python

import math
print(math.copysign(3, -5))  # Output: -3.0

# fsum(seq) : Return an accurate floating point sum of values in the iterable seq.
# Python

import math
print(math.fsum([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]))  # Output: 1.0

# math.isfinite(x): Returns True if ( x ) is neither an infinity nor a NaN (Not a Number).
# Python

import math
print(math.isfinite(10))  # Output: True

# math.modf(x): Returns the fractional and integer parts of ( x ).
# Python

import math
print(math.modf(4.5))  # Output: (0.5, 4.0)

# math.trunc(x): Returns the truncated integer value of ( x ).
# Python

import math
print(math.trunc(4.7))  # Output: 4

# math.log10(x): Returns the base '10' logarithm of ( x ).
# Python

import math
print(math.log10(100))  # Output: 2.0

# math.pow(x, y): Returns ( x ) raised to the power ( y ).
# Python

import math
print(math.pow(2, 3))  # Output: 8.0

# math.pi: Mathematical constant ( \pi ).
# Python

import math
print(math.pi)  # Output: 3.141592653589793

# math.e: Mathematical constant ( e ).
# Python

import math
print(math.e)  # Output: 2.718281828459045


#######################################################################################################
#######################################################################################################
#######################################################################################################

# +---+  |\  /|  +---+  --+--  |   |
# |      | \/ |  |   |    |    |   |
# |      |    |  +---+    |    +---+
# |      |    |  |   |    |    |   |
# +---+  |    |  |   |    |    |   |


# 1. cmath module: Used for complex number mathematical operations.
# Python

import cmath


# 2. cmath.sqrt(x): Returns the square root of a complex number ( x ).
# Python

print(cmath.sqrt(4))         # Output: (2+0j)
print(cmath.sqrt(-4))        # Output: 2j


# 3. cmath.exp(x): Returns ( e^x ) for a complex number ( x ).
# Python

print(cmath.exp(1))          # Output: (2.718281828459045+0j)
print(cmath.exp(1j))         # Output: (0.5403023058681398+0.8414709848078965j)


# 4. cmath.log(x[, base]): Returns the logarithm of ( x ) to the given base. Base defaults to e.
# Python

print(cmath.log(1))          # Output: 0j
print(cmath.log(-1))         # Output: 3.141592653589793j


# 5. cmath.log10(x): Returns the base-10 logarithm of ( x ).
# Python

print(cmath.log10(100))      # Output: (2+0j)
print(cmath.log10(-100))     # Output: (2+1.3643763538418412j)


# 6. cmath.phase(x): Returns the phase angle ( argument ) of a complex number ( x ) in radians.
# Python

print(cmath.phase(1 + 1j))   # Output: 0.7853981633974483


# 7.cmath.polar(x): Converts a complex number ( x ) to polar coordinates ( r, φ ).
# Python

print(cmath.polar(1 + 1j))   # Output: (1.4142135623730951, 0.7853981633974483)


# 8. cmath.rect(r, φ): Converts polar coordinates ( r, φ ) to a complex number.
# Python

print(cmath.rect(2, cmath.pi / 2))  # Output: (1.2246467991473532e-16+2j)


# 9. cmath.isinf(x): Returns True if either the real or imaginary part of ( x ) is infinite.
# Python

print(cmath.isinf(complex(float('inf'), 0)))  # Output: True


# 10. cmath.isnan(x): Returns True if either the real or imaginary part of ( x ) is NaN.
# Python

print(cmath.isnan(complex(float('nan'), 0)))  # Output: True


# 11. cmath.sin(x): Returns the sine of ( x ) in radians.
# Python

print(cmath.sin(cmath.pi / 2))  # Output: (1+0j)


# 12. cmath.cos(x): Returns the cosine of ( x ) in radians.
# Python

print(cmath.cos(0))  # Output: (1+0j)


# 13.cmath.tan(x): Returns the tangent of ( x ) in radians.
# Python

print(cmath.tan(cmath.pi / 4))  # Output: (0.9999999999999999+0j)


# 14. cmath.asin(x): Returns the inverse sine ( arcsin ) of ( x ).
# Python

print(cmath.asin(1))  # Output: (1.5707963267948966-0j)


# 15. cmath.acos(x): Returns the inverse cosine ( arccos ) of ( x ).
# Python

print(cmath.acos(1))  # Output: 0j


# 16. cmath.atan(x): Returns the inverse tangent ( arctan ) of ( x ).
# Python

print(cmath.atan(1))  # Output: (0.7853981633974483+0j)


# 17. cmath.sinh(x): Returns the hyperbolic sine of ( x ).
# Python

print(cmath.sinh(1))  # Output: (1.1752011936438014+0j)


# 18. cmath.cosh(x): Returns the hyperbolic cosine of ( x ).
# Python

print(cmath.cosh(1))  # Output: (1.5430806348152437+0j)


# 19. cmath.tanh(x): Returns the hyperbolic tangent of ( x ).
# Python

print(cmath.tanh(1))  # Output: (0.7615941559557649+0j)


# 20. cmath.asinh(x): Returns the inverse hyperbolic sine of ( x ).
# Python

print(cmath.asinh(1))  # Output: (0.881373587019543+0j)


# 21. cmath.acosh(x): Returns the inverse hyperbolic cosine of ( x ).
# Python

print(cmath.acosh(2))  # Output: (1.3169578969248166+0j)


# 22. cmath.atanh(x): Returns the inverse hyperbolic tangent of ( x ).
# Python

print(cmath.atanh(0.5))  # Output: (0.5493061443340548+0j)


# 23. cmath.pi: Mathematical constant ( \pi ).
# Python

print(cmath.pi)  # Output: 3.141592653589793


# 24. cmath.e: Mathematical constant ( e ).
# Python

print(cmath.e)  # Output: 2.718281828459045


#######################################################################################################
#######################################################################################################
#######################################################################################################

# +---+  +---+  |    |  +-+    +---+  |\    /|
# |   |  |   |  |\   |  |  \   |   |  | \  / |
# +---+  +---+  | \  |  |   \  |   |  |  \/  |
# |\     |   |  |  \ |  |   /  |   |  |      |
# | \    |   |  |   \|  |  /   |   |  |      |
# |  \   |   |  |    |  +-+    +---+  |      |


# 1. random.random()
# Generates a random float number between 0.0 and 1.0.
# Python

import random
print(random.random())
# Output: A random float between 0.0 and 1.0

# 2. random.randint(a, b)
# Returns a random integer between a and b (both inclusive).
# Python

print(random.randint(1, 10))
# Output: A random integer between 1 and 10

# 3. random.choice(seq)
# Returns a random element from a non-empty sequence.
# Python

my_list = [1, 2, 3, 4, 5]
print(random.choice(my_list))
# Output: A random element from the list

# 4. random.choices(seq, k=N)
# Returns a list with N random elements from the sequence, allowing duplicates.
# Python

print(random.choices(my_list, k=3))
# Output: A list with 3 random elements from the list

# 5. random.shuffle(seq)
# Shuffles the sequence in place.
# Python

random.shuffle(my_list)
print(my_list)
# Output: The list shuffled in place

# 6. random.sample(seq, k)        
# Returns a list with k unique random elements from the sequence.
# Python

print(random.sample(my_list, k=3))      
# Output: A list with 3 unique random elements from the list

# 7. random.uniform(a, b)          
# Returns a random float number between a and b.
# Python

print(random.uniform(1.5, 10.5))     
# Output: A random float between 1.5 and 10.5

# 8. random.triangular(low, high, mode)
# Returns a random float number between low and high, with the mode specifying the most frequent value.

print(random.triangular(1.0, 10.0, 5.0))
# Output: A random float between 1.0 and 10.0, with 5.0 being the most frequent value


#######################################################################################################
#######################################################################################################
#######################################################################################################

# +---+  --+--  +---+ --+--  -+-  +---+  --+-- -+-  +---+  +---+
# |        |    |   |   |     |   |        |    |   |      |
# +---+    |    +---+   |     |   +---+    |    |   |      +---+
#     |    |    |   |   |     |       |    |    |   |          |
# +---+    |    |   |   |    -+-  +---+    |   -+-  +---+  +---+


import statistics

# 1. statistics.mean(data)
# Calculates the arithmetic mean (average) of the data.

data = [12, 15, 18, 20, 22]
mean_value = statistics.mean(data)
print("Mean:", mean_value)
# Output: Mean: 17.4

# 2. statistics.median(data)
# Finds the median (middle value) of the data.

median_value = statistics.median(data)
print("Median:", median_value)
# Output: Median: 18

# 3. statistics.mode(data)
# Returns the mode (most common value) of the data.

data = [10, 15, 20, 15, 25, 30, 15]
mode_value = statistics.mode(data)
print("Mode:", mode_value)
# Output: Mode: 15

# 4. statistics.stdev(data)
# Calculates the standard deviation of the data.

data = [5, 8, 10, 12, 15]
std_deviation_value = statistics.stdev(data)
print("Standard Deviation:", std_deviation_value)
# Output: Standard Deviation: 3.8078865529319543

# 5. statistics.variance(data)
# Calculates the variance of the data.

variance_value = statistics.variance(data)
print("Variance:", variance_value)
# Output: Variance: 14.5

# 6. statistics.fmean(data)
# Calculates the fast, floating-point arithmetic mean of the data.

fmean_value = statistics.fmean(data)
print("Fast Mean:", fmean_value)
# Output: Fast Mean: 10.0

# 7. statistics.geometric_mean(data)
# Calculates the geometric mean of the data.

geometric_mean_value = statistics.geometric_mean(data)
print("Geometric Mean:", geometric_mean_value)
# Output: Geometric Mean: 9.032962962962964

# 8. statistics.harmonic_mean(data)
# Calculates the harmonic mean of the data.

harmonic_mean_value = statistics.harmonic_mean(data)
print("Harmonic Mean:", harmonic_mean_value)
# Output: Harmonic Mean: 8.0

# 9. statistics.median_low(data)
# Finds the low median of the data.

median_low_value = statistics.median_low(data)
print("Median Low:", median_low_value)
# Output: Median Low: 10

# 10. statistics.median_high(data)
# Finds the high median of the data.

median_high_value = statistics.median_high(data)
print("Median High:", median_high_value)
# Output: Median High: 10

# 11. statistics.median_grouped(data)
# Calculates the median of grouped data.

data = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
median_grouped_value = statistics.median_grouped(data)
print("Median Grouped:", median_grouped_value)
# Output: Median Grouped: 5.5

# 12. statistics.multimode(data)
# Returns a list of the most common values in the data.

data = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5]
multimode_value = statistics.multimode(data)
print("Multimode:", multimode_value)
# Output: Multimode: [4, 5]

# 13. statistics.quantiles(data, n)
# Divides the data into n intervals with equal probability.

quantiles_value = statistics.quantiles(data, n=4)
print("Quantiles:", quantiles_value)
# Output: Quantiles: [2.5, 4.0, 5.0]

# 14. statistics.pstdev(data)
# Calculates the population standard deviation of the data.

data = [5, 8, 10, 12, 15]
pstdev_value = statistics.pstdev(data)
print("Population Standard Deviation:", pstdev_value)
# Output: Population Standard Deviation: 3.415650255319866

# 15. statistics.pvariance(data)
# Calculates the population variance of the data.

pvariance_value = statistics.pvariance(data)
print("Population Variance:", pvariance_value)
# Output: Population Variance: 11.666666666666666

# 16. statistics.correlation(x, y)
# Calculates the Pearson correlation coefficient between two datasets.

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
correlation_value = statistics.correlation(x, y)
print("Correlation:", correlation_value)
# Output: Correlation: 1.0

# 17. statistics.covariance(x, y)
# Calculates the covariance between two datasets.

covariance_value = statistics.covariance(x, y)
print("Covariance:", covariance_value)
# Output: Covariance: 5.0

# 18. statistics.quantiles(data, n)
# Divides the data into n intervals with equal probability.

quantiles_value = statistics.quantiles(data, n=4)
print("Quantiles:", quantiles_value)
# Output: Quantiles: [6.5, 10.0, 13.5]


#######################################################################################################
#######################################################################################################
#######################################################################################################

# +---+  \     /  +---+
# |       \   /   |
# +---+    \ /    +---+
#     |     |         |
# +---+     |     +---+


# sys module: Provides access to some variables used or maintained by the Python interpreter.
# Python

import sys

# sys.version: Returns the version of the Python interpreter.
# Python

print(sys.version)  # Output: e.g., '3.11.4 (main, Jul  5 2023, 13:38:37) [GCC 12.2.0]'

# sys.version_info: Returns a tuple containing the five components of the version number.
# Python

print(sys.version_info)  # Output: sys.version_info(major=3, minor=11, micro=4, releaselevel='final', serial=0)

# sys.platform: Returns the platform identifier.
# Python

print(sys.platform)  # Output: e.g., 'win32', 'linux', 'darwin' (for macOS)

# sys.path: Returns the list of strings that specifies the search path for modules.
# Python

print(sys.path)  # Output: List of directory paths

# sys.argv: List of command-line arguments passed to a Python script.
# Python

print(sys.argv)  # Output: ['script_name.py', 'arg1', 'arg2', ...]

# sys.exit([arg]): Exits from Python. Optional arg is the exit status (defaults to zero).
# Python

sys.exit()  # This will exit the program immediately
# Argument can contain numbers and strings.
# Number '0' represent No Error Exit while all other represent some kind of Error in the input or file presence.....etc.
# Any String gets printed before exiting if passed as the argument.

# sys.stdin: Standard input stream (usually for reading from user input).
# Python

user_input = sys.stdin.readline()
print(user_input)

# sys.stdout: Standard output stream (used for print).
# Python

sys.stdout.write("Hello from sys.stdout\n")  # Output: Hello from sys.stdout

# sys.stderr: Standard error stream (used for error messages).
# Python

sys.stderr.write("This is an error message\n")  # Output: This is an error message

# sys.getsizeof(object): Returns the size (in bytes) of an object.
# Python

print(sys.getsizeof(123))  # Output: 28 (can vary by system)

# sys.modules: Dictionary of all modules that have been imported.
# Python

print('math' in sys.modules)  # Output: True or False depending on import

# sys.maxsize: The largest integer a variable can take.
# Python

print(sys.maxsize)  # Output: e.g., 9223372036854775807 on a 64-bit system

# sys.builtin_module_names: Tuple of names of all built-in modules.
# Python

print(sys.builtin_module_names)  # Output: e.g., ('sys', 'builtins', ...)

# sys.getrecursionlimit(): Returns the current recursion limit.
# Python

print(sys.getrecursionlimit())  # Output: e.g., 1000

# sys.setrecursionlimit(limit): Sets the maximum recursion depth.
# Python

sys.setrecursionlimit(1500)
print(sys.getrecursionlimit())  # Output: 1500

# sys.flags: Returns flags passed to the Python interpreter.
# Python

print(sys.flags)  # Output: sys.flags(debug=0, inspect=0, ...)

# sys.executable: Path of the Python interpreter binary.
# Python

print(sys.executable)  # Output: e.g., '/usr/bin/python3'


#######################################################################################################
#######################################################################################################
#######################################################################################################

# --+-- --+-- |\    /| +----
#   |     |   | \  / | |
#   |     |   |  \/  | +--
#   |     |   |      | |
#   |   --+-- |      | +----


# time module: Provides time-related functions.
# Python

import time

# time.time(): Returns the current time in seconds since the epoch (January 1, 1970).
# Python

print(time.time())  # Output: 1718192761.123456 (varies)

# time.sleep(seconds): Suspends execution for the given number of seconds.
# Python

time.sleep(2)  # Pauses program for 2 seconds

# time.ctime([secs]): Converts a time in seconds to a readable string.
# Python

print(time.ctime())  # Output: 'Thu Jun 12 15:46:12 2025'

# time.gmtime([secs]): Converts a time expressed in seconds since epoch to UTC.
# Python

print(time.gmtime(0))  # Output: <<<time.struct_time(tm_year=1970, ...)>>>

# time.localtime([secs]): Converts seconds since epoch to local time.
# Python

print(time.localtime())  # Output: <<<time.struct_time(tm_year=2025, ...)>>>

# time.strftime(format[, t]): Converts a struct_time to a string according to format.
# Python

print(time.strftime("%Y-%m-%d %H:%M:%S"))  # Output: '2025-06-12 15:46:12'

# time.strptime(string, format): Parses a string representing time into struct_time.
# Python

print(time.strptime("2025-06-12", "%Y-%m-%d"))  # Output: <<<time.struct_time(...)>>>

# time.asctime([t]): Converts struct_time to a readable string.
# Python

print(time.asctime(time.localtime()))  # Output: 'Thu Jun 12 15:46:12 2025'

# time.mktime(t): Converts a struct_time to seconds since epoch.
# Python

t = time.localtime()
print(time.mktime(t))  # Output: <<<Seconds since epoch>>>

# time.perf_counter(): Returns a high-precision timer for benchmarking.
# Python

start = time.perf_counter()
# <<<Some code here>>>
end = time.perf_counter()
print(end - start)  # Output: <<<Execution time in seconds>>>

# time.process_time(): Returns CPU time used by the process.
# Python

start = time.process_time()
# <<<Some code here>>>
end = time.process_time()
print(end - start)  # Output: <<<CPU time used>>>


#######################################################################################################
#######################################################################################################
#######################################################################################################

# +--+  +---+ --+-- +----    --+-- --+-- |\    /| +----
# |  ++ |   |   |   |          |     |   | \  / | |
# |   | +---+   |   +--   --   |     |   |  \/  | +--
# |  ++ |   |   |   |          |     |   |      | |
# +--+  |   |   |   +----      |   --+-- |      | +----


# datetime module: Supplies classes for manipulating dates and times.
# Python

import datetime


# datetime.datetime.now(): Returns current local date and time.
# Python

print(datetime.datetime.now())  # Output: 2025-06-12 16:00:00.123456


# datetime.datetime.today(): Returns current local date and time (same as now()).
# Python

print(datetime.datetime.today())  # Output: 2025-06-12 16:00:00.123456


# datetime.datetime.utcnow(): Returns current UTC date and time.
# Python

print(datetime.datetime.utcnow())  # Output: 2025-06-12 10:30:00.123456


# datetime.date.today(): Returns the current local date.
# Python

print(datetime.date.today())  # Output: 2025-06-12


# datetime.datetime(year, month, day, hour, minute, second): Creates a datetime object.
# Python

dt = datetime.datetime(2025, 1, 1, 12, 0, 0)
print(dt)  # Output: 2025-01-01 12:00:00


# datetime.date(year, month, day): Creates a date object.
# Python

d = datetime.date(2025, 6, 12)
print(d)  # Output: 2025-06-12


# datetime.time(hour, minute, second): Creates a time object.
# Python

t = datetime.time(14, 30, 0)
print(t)  # Output: 14:30:00


# datetime.datetime.strftime(format): Formats datetime object into string.
# Python

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Output: 2025-06-12 16:00:00


# datetime.datetime.strptime(string, format): Parses string into datetime object.
# Python

dt = datetime.datetime.strptime("2025-06-12 14:00:00", "%Y-%m-%d %H:%M:%S")
print(dt)  # Output: 2025-06-12 14:00:00


# datetime.timedelta: Represents a duration or difference between dates/times.
# Python

delta = datetime.timedelta(days=5)
print(datetime.date.today() + delta)  # Output: 2025-06-17


# datetime.datetime.date(): Extracts the date part from a datetime object.
# Python

now = datetime.datetime.now()
print(now.date())  # Output: 2025-06-12


# datetime.datetime.time(): Extracts the time part from a datetime object.
# Python

now = datetime.datetime.now()
print(now.time())  # Output: 16:00:00.123456


# datetime.datetime.weekday(): Returns the weekday (0 = Monday, 6 = Sunday).
# Python

print(datetime.date(2025, 6, 12).weekday())  # Output: 3 (Thursday)


# datetime.datetime.isoweekday(): Returns the ISO weekday (1 = Monday, 7 = Sunday).
# Python

print(datetime.date(2025, 6, 12).isoweekday())  # Output: 4 (Thursday)


# datetime.datetime.isoformat(): Returns ISO 8601 formatted string.
# Python

print(datetime.datetime.now().isoformat())  # Output: '2025-06-12T16:00:00.123456'


#######################################################################################################
#######################################################################################################
#######################################################################################################

# +---+  +---+  +---+  \     /
# |      |   |  |   |   \   /
# |      |   |  +---+    \ /
# |      |   |  |         |
# +---+  +---+  |         |


# The copy module is used to duplicate objects, providing shallow and deep copying.

# copy.copy(x): Returns a shallow copy of object ( x ).
# Python

import copy
lst = [1, 2, [3, 4]]
shallow = copy.copy(lst)
print(shallow)  # Output: [1, 2, [3, 4]]

# copy.deepcopy(x): Returns a deep copy of object ( x ).
# Python

import copy
lst = [1, 2, [3, 4]]
deep = copy.deepcopy(lst)
print(deep)  # Output: [1, 2, [3, 4]]

# Difference demonstration (shallow vs deep)
# Python

import copy
lst = [1, 2, [3, 4]]

shallow = copy.copy(lst)
deep = copy.deepcopy(lst)

lst[2].append(5)

print(shallow)  # Output: [1, 2, [3, 4, 5]]
print(deep)     # Output: [1, 2, [3, 4]]

# copy.copy() does NOT copy nested objects (references are shared)
# copy.deepcopy() copies all nested objects recursively

# Copying immutable objects (no real effect)
# Python

import copy
x = 10
y = copy.copy(x)
z = copy.deepcopy(x)

print(x, y, z)  # Output: 10 10 10

# Copying dictionary using shallow copy
# Python

import copy
d = {"a": 1, "b": [2, 3]}
d_copy = copy.copy(d)
print(d_copy)  # Output: {'a': 1, 'b': [2, 3]}

# Copying dictionary using deep copy
# Python

import copy
d = {"a": 1, "b": [2, 3]}
d_deep = copy.deepcopy(d)
print(d_deep)  # Output: {'a': 1, 'b': [2, 3]}

# Manual shallow copy alternatives (built-in)
# Python

lst = [1, 2, 3]
lst2 = lst[:]          # slice copy
lst3 = list(lst)       # list constructor
lst4 = lst.copy()      # list method

print(lst2, lst3, lst4)

# Manual shallow copy for dict
# Python

d = {"x": 1, "y": 2}
d2 = d.copy()
print(d2)  # Output: {'x': 1, 'y': 2}


#######################################################################################################
#######################################################################################################
#######################################################################################################

# +---+  +---+  +---+  +   +  +     +---+  +---+
# |   |  |      |      |   |  |     |   |  |   |
# +---+  +---+  | +-+  |   |  |     +---+  +---+
# | \    |      |   |  |   |  |     |   |  | \
# |  \   +---+  +---+  +---+  +---+ |   |  |  \


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


#######################################################################################################
#######################################################################################################
#######################################################################################################

# ---+---  +---+  +---+  |\    |
#    |     |      |   |  | \   |
#    |     +---+  |   |  |  \  |
# ^  |         |  |   |  |   \ |
# +--+     +---+  +---+  |    \|

import json
"""
The JSON module in Python is used to convert data between Python objects and JSON (JavaScript Object Notation) format.
JSON is a lightweight, text-based data interchange format commonly used for data storage and data transfer between systems.
"""
"""
| Python Type | JSON Type |
| ----------- | --------- |
| dict        | object    |
| list        | array     |
| tuple       | array     |
| str         | string    |
| int, float  | number    |
| True        | true      |
| False       | false     |
| None        | null      |
"""
"""
Only double quotes ("...") can be used inside a JSON File.
No capital letters for Booleans
"""

# 1) json.dumps()  → Python object  ➜ JSON STRING
#    "dump to STRING"
data = {"name": "Alice", "age": 20}
json_str = json.dumps(data)                       # Python dict → JSON text (string)
print(json_str)                                   # '{"name": "Alice", "age": 20}'
print(type(json_str))                             # <class 'str'>


# 2) json.loads()  → JSON STRING ➜ Python object
#    "load from STRING"
json_str = '{"name": "Alice", "age": 20}'         # JSON text

data = json.loads(json_str)                       # JSON text (string) → Python dict
print(data)                                       # {'name': 'Alice', 'age': 20}
print(type(data))                                 # <class 'dict'>


# 3) json.dump()  → Python object ➜ JSON in FILE
#    "dump to FILE"  (FILE HANDLING)
data = {"name": "Bob", "age": 25}

with open("student.json", "w", encoding="utf-8") as f:
    json.dump(data, f)                            # writes JSON directly into file f

# After this, student.json file contains: {"name": "Bob", "age": 25}


# 4) json.load()  → JSON in FILE ➜ Python object
#    "load from FILE"  (FILE HANDLING)
with open("student.json", "r", encoding="utf-8") as f:
    data_from_file = json.load(f)                 # reads JSON from file and converts to dict
print(data_from_file)                             # {'name': 'Bob', 'age': 25}

"""
→ json.dump() and json.load() are used for FILE HANDLING because:
  • json.dump() writes JSON directly into a file object (no extra string step).
  • json.load() reads JSON directly from a file object and converts it to Python.
  • They work with file pointers (fp), so they are convenient and memory‑efficient when the goal is to store or read JSON data from files.
"""

# Indenting the json dictionary

data = {"name": "Alice", "age": 30, "skills": ["Python", "SQL"]}
print(json.dumps(data))
print(json.dumps(data, indent=4))
"""
{"name": "Alice", "age": 30, "skills": ["Python", "SQL"]}

{
    "name": "Alice",
    "age": 30,
    "skills": [
        "Python",
        "SQL"
    ]
}
"""
