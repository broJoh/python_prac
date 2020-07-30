# Some rational numbers can not be represented using a finite number of digits
# Numbers in a computer are represented using bits, not decimal digits, so
# instead of powers of 10 it uses powers of 2
# Some decimal numbers have a finite binary representation and that means
# an exact float representation, and other an infinite binary representation
# and that means an approximate fload representation

# We can't use the == operator to check the equality of floats. We must use the 
# isclose() function of the math module or the decimal modules


# a = 0.1 + 0.1 + 0.1
# b = 0.3
# a == b -----> False (왜냐면 실제 파이썬에서 저장하는 수치로는 미묘한 차이가 생긴다.)
# 확인할 때 format(a, '.25f') 이용하면 된다.

a = 3.4
b = 2.3

c = a + b
print(c)