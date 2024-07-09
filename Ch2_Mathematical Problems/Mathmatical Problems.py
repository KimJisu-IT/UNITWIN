
# N = 27, steps = 111
# -------------------------------
N = int(input("Enter a number : "))
step = 0

while N > 1:
    if N % 2 == 0:
        N = N // 2
    elif N % 2 == 1:
        N = 3*N + 1
    print(N)
    step += 1

print('steps =', step)


# List
# --------------------------------
color = ['red', 'blue', 'green']
color[0]
color[2]
color[-1]
len(color)
color*2
'blue' in color
for c in color:
    print(c)

for i, c in enumerate(color):
    print("{}th color is {}".format(i+1, c))

num = [1, 2, 3]
color + num
color[0] = 'yellow'
color.append('white')
color
color.remove('white')
color
del color[0]


# List of Fibonacchi numbers
# --------------------------------
n = 100
Fn = [0, 1]

for i in range(2, n+1):
    Fn.append(Fn[-1]+Fn[-2])

print(Fn)