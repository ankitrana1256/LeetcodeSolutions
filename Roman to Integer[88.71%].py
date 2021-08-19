s = "CC"
res = 0
nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
l = len(s)
i = 0
while(i < l):
    print("i :",i)
    if i + 1 < len(s) and s[i] + s[i+1] in nums:
        print(s[i] + s[i+1])
        res += nums[s[i] + s[i+1]]
        i += 2
    else:
        res += nums[s[i]]
        print(res)
        i += 1
print(res)