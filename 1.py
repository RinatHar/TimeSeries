a, b = 56, 274

x = 0
result = 0

plus = 1

while x <= b:
    if (x == 0):
        x += plus
    elif (x % 10 == 9):
        if x >= a:
            result += 1
        x += plus + 1
        plus = plus * 10 + 1
    elif (x // 10 == 0):
        if x >= a:
            result += 1
        x += 1
    elif (x > 10):
        if x >= a:
            result += 1
        x += plus
    

print(result)