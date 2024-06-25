# 02. Conditional statement

# Code block and indentation
# Exercise 1 ---------------------
a = 4       # define
b = -3

if (a * b < 0) :
    print("a, b has different sign.")

    if a < 0:
        print("a < 0")
        print(a)
    else:
        print(b)

# >> a, b has different sign.
# >> -3


# Exercise 2 ---------------------
a = 0
b = -2

if (a * b < 0) :
    print("a, b has different sign.")

    if a < 0:
        print("a < 0")
        print(a)
    else:
        print(b)

# >> a, b has different sign.
# >> -3


# Conditional statement - example
# --------------------------------
h = 0
m = 23

if m > 30:
    print(h, ':', m - 30)
elif m < 30:
    if h > 0:
        print(h - 1, ':', m + 30)
    elif h == 0:
        print(23, ':', m + 30)

# >> 23 : 53


# --------------------------------
h = 13
m = 33

if m >= 40:
    print(h, ':', m - 30)
elif m >= 30:
    print(h, ': 0' + str(m - 30))    # (h, ': 0', str(m - 30)) | print >> 13 : 0 3
elif m < 30:
    if h > 0:
        print(h - 1, ':', m + 30)
    elif h == 0:
        print(23, ':', m + 30)

# >> 13 : 03


# Conditional statement - (Collatz Conjecture)
# --------------------------------------------


# Loops & range(start, stop, step)
# ---------------
L = range(1, 20, 3)
L           # >> range(1, 20, 3)
list(L)     # >> [1, 4, 7, 10, 13, 16, 19]
for i in L:
    print(i)


# print() & format()
# ------------------
print('111 divided by 4 is', 111/4)
print('{} divided by {} is {}'.format(111, 4, 111/4))
print('{0} divided by {1} is {2}'.format(111, 4, 111/4))

N = 6
for i in range (1, 10):
    print('{} x {} = {}'.format(N, i, N * i))



# While Loops
N = 10
while N > 5:
    print(N)
    N -= 1

N = 10
while True:
    print(N)
    N -= 1
    if N == 5:
        break

number = int(input('Enter a number: '))
total = 0

while number != 0:
    total += number
    number = int(input('Enter a number: '))

print('The sum is ', total)


# A number guessing game

import random

solution = random.randint(1, 100)
noftry = 0

while True:
    number = int(input("Guess the number: "))
    noftry += 1

    if number > solution:
        print('It is too big')
    elif number <solution:
        print('It is too small')
    elif number == solution:
        print("Perfect")
        print('You found the number in {} tries'.format(noftry))
        break