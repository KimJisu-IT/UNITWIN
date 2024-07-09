# quotient, remainder, '' quotation mark

# 01.
Celsius = int(input('01. Enter a number: '))
Fahrenheit = Celsius + 32
print(Fahrenheit)


# 02.
year = int(input('02. Enter a number: '))

if year % 4 == 0 & year % 100 != 0:
    print(str(year)+ ' is a leap year')
elif year % 400 == 0:
    print(str(year)+ ' is a leap year')
else:
    print(str(year)+' is a given year')


# 03.
x = int(input('03. Enter a number: '))

if x >= 30:
    print(x-30)
elif x < 30:
    print(x+30)


# 04.
for i in range(1, 21):
    if (i % 3 != 0):
        print(i)


# 05.
square =[]
num = 2
answer = 0

for i in range(1, 11):
    answer = num * num
    square.append(answer)
    num = answer

print(square)


# 06.
answer = 0

for i in range(1, 101):
    if (i % 3 == 1):
        answer += i
print(answer)   # 1717


# 07.
answer = 0

for i in range(1, 21):
    answer += (1 / (2 * i + 1))
print(answer)


# 08. 
n = 0
n = int(input('08. Enter a number: '))
divisorList = []

for i in range(1, n + 1):
    if (n % i == 0):
        divisorList.append(i)

print(divisorList)


# 09.
answer = 0
n = 0
n = int(input('09. Enter a number: '))

for i in range(1, n + 1):
    if (n % i == 0):
        answer += i

print(answer)


# 10.
answer = 1
n = 0
n = int(input('10. Enter a number: '))

for i in range(1, n+1):
    answer *= i

print(answer)


# 11.
n = 5587763
a = 0
b = 0
for i in range(2, 10000):
    if (n % i == 0):
        print(i)        # 809, 6907


# 12.
for i in range(2, 31):
    print(2 ** i -2)


# 13.
number = 840

for i in range (1, 101):
    if (52**3 + (23**3 % (840 * i))) == 0:
        print(i)


# 14.
k = 0
for i in range(1, 101):
    if (10 ** 19 - 2 ** 19 ) == 2 ** k:
        print(i)




# 15.
min = 10001
for i in range(1, 101):
    number = i*i - 40 * i + 3
    if (number < min):
        min = number

print(min)      # -397

'''
min = 10001
cnt = 0
for i in range(0, 101):
    number = i**2 - 40*i + 3
    if (number < min):
        min = number
        cnt = i
        print(i, min)       # i = 20, min = -397

print(min)
'''

# 16.
answer = 0
cnt = 0
r = 0.05
P = 100

while(1):
    P = P*(1+r)
    cnt += 1
    # print(P)
    if (P >= 100*2):
        print(cnt)
        break
