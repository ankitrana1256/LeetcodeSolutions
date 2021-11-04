s = "pwwkew"
char = []
l = len(s)
temp = 0
end = 0
while(end < l):
    word = s[end:]    
    print(word)        
    for i, c in enumerate(word):
        if c not in char:
            char.append(c)
            word = "".join(char)
        else:
            char.clear()
            break
    new_length = len(word)
    if new_length >= temp:
        temp = new_length
    end += 1
print(temp)