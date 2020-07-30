# In python3 a string is an ordered sequence of UNICODE characters. Unicode is an ASCII
'''
이걸로도 주석처리 가능
'''

#### Get user input ####

'''
print('An example of using the input() function')
name = input("Enter your name:")
print('Type:', type(name))
print('Your name is:', name)
'''


# string to int

# c = 1.5
# c_float = float(c)
# c_int = int(c_float)

# or
# c_int = int(float(c))

# 위와같이 float로 먼저 변환하고 int로 전달해줘야한다.


# slicing

movie = 'The Godfother'
movie[0:2]  # == movie[:2]
# 'Th'

movie[0:5]
# 'e G'

movie[4:]
# 'Godfather'


# formating strings(F-Strings)

'The value {} in KM is {}'.format(miles, miles * 1.60934)
# 'The value 23.2 in KM is 37.336687...'


####################################
# String Indexing, Operations and Slicing
####################################

# A string can be treated like a list of characters. Indexing starts from 0
language = 'Python 3'
language[0]              # => 'P'
language[1]              # => 'y'
language[-1]             # => '3'
language[-2]             # => ' '
"This is a string"[0]    # => 'T'

# language[100]          # => IndexError: string index out of range

# Cannot modify a string, it's immutable
# language[0] = 'J'      # => TypeError: 'str' object does not support item assignment


# You can find the length of a string
len("This is a string")  # => 16


# Strings can be concatenated with + and repeated with *
print('Hello ' + 'world!')   # => 'Hello world!'
print('Hello ' * 3)          # => 'Hello Hello Hello '
print('PI:' + str(3.1415))   # => Can concatenate only strings


# Slicing returns a new string
# start index is included, end index is excluded
movie = 'Star Wars'
movie[0:4]    # => 'Star' -> from index 0 included to index 4 excluded
movie[:4]     # => 'Star' -> start index defaults to zero
# => 'ar Wars' -> end index defaults to the index of the last char of the string
movie[2:]
movie[::]     # => 'Star Wars'
# => 'ar Wars -> slicing doesn't return error when using index out of range
movie[2:100]
# => 'trW' -> the 3rd index is the step (from index 2 included to 6 excluded in steps of 2)
movie[1:6:2]
# => 'aW ra' -> from index 6 included to index 1 excluded in steps of -1 (backwards)
movie[6:1:-1]
movie[::-1]    # => 'sraW ratS -> reverses the string


#################################
# Formatting Strings
#################################
price = 1.33
quantity = 5

# f-string literals (Python 3.6+) - NEW!
f'The price is {price}'                    # => 'The price is 1.33'
f'Total value is {price * quantity}'       # => 'Total value is 6.65'
# => 'Total value is 6.6500' -> displaying with 4 decimals
f'Total value is {price * quantity:.4f}'

# Classical method
'The price is {}'.format(price)                      # => 'The price is 1.33'
# => 'The total value is 6.65'
'The total value is {}'.format(price * quantity)
# => 'The total value is 6.6500' -> displaying with 4 decimals
'The total value is {:.4f}'.format(price * quantity)


# => 'The price is 1.33 and the total value is 6.65'
'The price is {} and the total value is {}'.format(price, price * quantity)
# => 'The price is 1.33 and the total value is 6.65'
'The price is {0} and the total value is {1}'.format(price, price * quantity)
# => 'The total value is 6.65 and the price is 1.33'
'The total value is {1} and the price is {0}'.format(price, price * quantity)

# => 'The total value is 6.65'
print('The total value is ', price * quantity)
