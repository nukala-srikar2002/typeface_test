s1 = input()
s2 = input()
x = s2[-1]
count = 0
for i in s1:
    if i == x:
        count += 1
print(count)
