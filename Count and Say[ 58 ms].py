class Solution:
    def calc(r):
        temp = ""
        a = r + " "
        prev = a[0]
        count = 1
        for i in range(1,len(a)):
            if a[i] == prev:
                count += 1
            else:
                prev = a[i]
                temp += str(count) + a[i-1]
                count = 1
        return temp
    
    def countAndSay(n: int) -> str:
        result = ""
        if n == 1:
            result = "1" 
        else:
            i = 2
            temp = str(1)
            while(i <= n):
                result = Solution.calc(temp)
                temp = result
                i += 1
        return "Result : " + result
        
n = 100
output = Solution.countAndSay(n)
print(output)