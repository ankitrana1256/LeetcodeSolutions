class Solution:
    def reverseWords(s):
        text = s.split(" ")[::-1]
        print(text)
        res = []
        for ele in text:
            if ele.strip():
                res.append(ele)

        print(res)
        result = " ".join(res)
        return result
        

s = "  hello world  "
a = Solution.reverseWords(s)
print(a)