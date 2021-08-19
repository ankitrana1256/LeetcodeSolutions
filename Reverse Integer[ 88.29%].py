#x = 123 
x = -123
judge = False
        
if x < 0:
    x = -x
    judge = True

revs_no = 0

while(x>0):
    remainder = x % 10
    revs_no = (revs_no * 10) + remainder
    x = x // 10

if(judge):
    revs_no = -revs_no
else:
    revs_no = +revs_no
            
if revs_no < -2**31 or revs_no > 2**31 -1:
    revs_no = 0
else:
    revs_no
        
print(revs_no)