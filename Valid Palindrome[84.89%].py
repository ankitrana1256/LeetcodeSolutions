class Solution:
    def isPalindrome(s):
        s = list(s)
        res = []
        for i in s:
            if i.isalnum():
                res.append(i)
        given = "".join(res).lower()
        res = res[::-1]
        output = "".join(res).lower()
        if given == output:
            return True
        else:
            return False
        
    
s = "0p"
a = Solution.isPalindrome(s)
print(a)