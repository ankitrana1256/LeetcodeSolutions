strs = ["flower","flow","flight"]
strs.sort(key = len)
l = len(strs)
max_j = len(strs[0])
flag = False
prefix = ""
j = 0
while(j < max_j):
    match = strs[0][j]
    for i in range(l):
        a = strs[i][j]
        if a == match:
            flag = True
        else:
            flag = False
            break
    
    if flag:
        prefix += a
        j += 1
    else:
        j = max_j

print(prefix)