#s = "   +0 123"
#s = "4193 with words"
#s = "123-"
s = "  +  413"
new_alpha = ""
sign = 0
count = 0
flag = False
min_value = -2**31
max_value = 2**31 - 1

for i in s:
    if i != " ":
        if (i.isdigit()):
            new_alpha += i
            count += 1
        elif i == "-":
            sign += 1
            if count > 0:
                break
            else:
                flag = True
                
        elif i == "+":
            sign += 1
        else:
            break
        
    elif i == " " and ( count > 0 or sign > 0):
        break
        
    if sign == 2:
        break   
     

if sign <= 2:
    if new_alpha != "":
        if(flag):
            new_alpha = "-" + new_alpha
        else:
            new_alpha
    else:
        new_alpha = 0
else:
    new_alpha = 0


char = int(new_alpha)

if char < min_value: 
    char = min_value
elif char > max_value:
    char = max_value
else:
    char
        
print(char)