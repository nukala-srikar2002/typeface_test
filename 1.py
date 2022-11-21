n = int(input())
if n == 0:
    print(0)
a = []
while(n):
    rem = n%3
    n = n//3
    a.append(str(rem))
ternary = int("".join(reversed(a)))
print(ternary)
