class Solution:
    def isPowerOfTwo(n: int) -> bool:
        i = 0
        flag = None
        while flag is None:
            if 2**i == n:
                flag = True
                break
            
            if 2**i > n:
                flag = False
                break
            
            i+=1
        return flag
    
n = 16
a = Solution.isPowerOfTwo(n)
print(a)