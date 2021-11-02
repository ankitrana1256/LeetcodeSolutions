class Solution:
    def frequencySort(s: str):
        new = list(set(s))
        ct = {}
        temp = ""
        
        for i in new:
            charCount = s.count(i)
            ct[i] = charCount
            
        newdict = sorted(ct, key=ct.get, reverse=True)
        
        for j in newdict:
            word = j * ct[j]
            temp += word
            
        return temp
        
s = "tree"
a = Solution.frequencySort(s)
print(a)