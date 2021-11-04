# s = "babad"
s = "aacaaaaacaa"
r = s[::-1]
counted = []
temp = ""
count = 0

def morethntwo(index, count): 
    for m in range(len(index)):
        for k in range(m+1,len(index)):
            word = s[index[m]:index[k]+1]
            new_word = word[::-1]
            if word == new_word:
                length = len(word)
                if length > count:
                    count,temp = length, word
    return temp

for i in range(len(s)):  
    if s[i] not in counted:
        counted.append(s[i])
        index = [j for j, x in enumerate(s) if x == s[i]]
        
        if len(index) <= 2:
            word = s[index[0]:index[-1] + 1]
        else:
            word = morethntwo(index, count)
    
        new_length = len(word)
        if word in r:
            if new_length > count:
                count,temp = new_length,word            

print(f"\nYour word :{temp}")