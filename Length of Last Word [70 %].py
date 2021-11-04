class Solution:
    def lengthOfLastWord(s):
        a = s.split(" ")
        res = [i for i in a if i!='']
        return len(res[-1])
    
s = "   fly me   to   the moon  "
a = Solution.lengthOfLastWord(s)
print(a)  