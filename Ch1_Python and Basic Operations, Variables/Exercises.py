# Exercises

# 01_Print 2^n for n from 1 to 20
answer = 0
for i in range(1, 21):
    answer = 2 ** i
    print(answer)

answer = 0
for i in range(20):
    answer = 2 ** (i + 1)
    print(answer)

# 02_Write a code to add up all natural numbers 1 to 100
answer = 0
for i in range(1, 101):
    answer += i
print(answer)       # >> 5050


# 03_Can you add all even numbers between 1 and 100?
answer = 0
for i in range(2, 101, 2):
    answer += i
print(answer)       # >> 2550

answer = 0
for i in range(1, 101):
    if (i % 2) == 0:        # even number
        answer += i
print(answer)       # >> 2550


# 04
a = 0
b = 3.141592 ** 2 / 6

for i in range(1, 100001):
    a += 1 / i**2

print(a)            # >> 1.6449240668982423
print(b)            # >> 1.6449333824106669


# 05_Print all integers between 1 and 100 which are divisible by 3, but not divisible by 2.
# How many are there?
count = 0

for i in range(1, 101):
    if (i % 3 == 0) & (i % 2 != 0):     # if (i % 3 == 0) and (i % 2 != 0):
        print(i)
        count += 1

print(count)        # >> 17


# 06_If you put P dollars in your bank, after one year it becomes P(1+r) when the interest rate is r.
# When r = 0.07 and P = 100, what is the amount with interest added after 10 years?
P = 100
r = 0.07

for i in (1, 11):
    P *= (1 + r)

print(P)        # >> 114.49000000000001


# 07_Print all integer triples (a, b, c) such that a + b + c = 10 and a >= b >= c > 0.
# How many are there?
count = 0

for a in range(1, 11):
    for b in range(1, a + 1):
        for c in range(1, b + 1):
            if a + b + c == 10:
                print(c, b, a)
                count += 1

print(count)        # >> 8