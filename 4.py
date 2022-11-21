a = []
n = 256
for i in range(n):
    a.append(list(map(int,input().split())))
tl, tr, bl, br = 255, 0, 255, 0
res = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 0:
            if i < tl and i < bl:
                tl = bl = i
            if j > tr:
                tr = br = j
            
        if a[i][j] == 0:
            if i > tl and i > tr:
                tr = i
            if j > bl and j > br:
                br = j
res.append((tl,bl))
res.append((tr,br))
res.append((bl,tl))
res.append((br,tr))
for i in res:
    print(i)
