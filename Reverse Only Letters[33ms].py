class Solution(object):
    def reverseOnlyLetters(s):
        p = list(s)
        word = []
        for i in range(len(p)):
            if p[i].isalpha():
                word.append(p[i])
                p[i] = 0
        word = word[::-1]
        
        for j in range(len(p)):
            if p[j] == 0:
                p[j] = word[0]
                word.pop(0)
        
        result = "".join(p)
        return result
    
s = "Test1ng-Leet=code-Q!"
# s = "ab-cd"
a = Solution.reverseOnlyLetters(s)