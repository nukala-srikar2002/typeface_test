a = [0,1,2,5,6,8,9]
n = int(input())
x = 1
while(n):
    y = x
    while(y):
        r = y%10
        if r not in a:
            break
        y = y//10
        
    if y == 0:
        n -= 1
    if n == 0:
        print(x)
    x += 1
