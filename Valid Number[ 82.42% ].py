# VALIDATE NUMBERS
#s = "0e1"
#s = "0"
#s = "2"
#s = "0089"
#s = "-0.1"
#s = "+3.14"
#s = "4."
#s = "-.9"
#s ="-90E3"
#s = "3e+7"
#s = "+6e-1"
#s = "53.5e93"
#s = "-123.456e789"

# NON VALIDATE NUMBERS
#s = "abc"
#s = "1a"
#s = "1e"
#s = "e3"
#s = "99e2.5"
#s = "--6"
#s = "-+3"
#s = "95a54e53"

# CODE
count = 0
flag = False
dot_count = 0
new_no = ""

for i in s:
    if i.isdigit():
        flag = False
        new_no += i
        count += 1
            
    if i == "-" or i == "+":
        if flag == False:
            new_no += i
            flag = True
        else:
            new_no = None
            break
        
    if i == ".":
        if dot_count < 1:
            dot_count += 1
            new_no += i
        else:
            new_no = None
            break
        
    if i.isalpha():
        if i == "e" or i == "E":
            if count >= 1:
                new_no += i
                count += 1
            else:
                new_no = None
                break
        else:
            new_no = None
            break

try:
    if new_no != None:    
        char = float(new_no)
        print(True)
    else:
        char = None
        print(False)
    
except ValueError:
    print(False)