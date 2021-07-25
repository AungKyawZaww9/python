'''import fractions

print(fractions.Fraction(1.5))

print(fractions.Fraction(5))

print(fractions.Fraction(1,3))

print("\n")

import fractions

# As float
# Output: 2476979795053773/2251799813685248
print(fractions.Fraction(1.1))

# As string
# Output: 11/10
print(fractions.Fraction('1.1'))

from fractions import Fraction as F

print(F(4, 3) + F(1, 3))

print(1 / F(5, 6))

print(F(-3, 10) > 0)

print(F(-3, 10) < 0)'''


import random

print(random.randrange(10, 20))

x = ['a', 'b', 'c', 'd', 'e']

# Get random choice
print(random.choice(x))

# Shuffle x
random.shuffle(x)

# Print the shuffled x
print(x)

# Print random element
print(random.random())
