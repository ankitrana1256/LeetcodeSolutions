class Solution:
    def addBinary(a, b):
        res = bin(int(a,2)+int(b,2))
        print(res[2:])
    
a = "11"
b = "1"
output = Solution.addBinary(a, b)
print(output)