class Solution:
    def subtractProductAndSum(n):
        l1 = list(str(n))
        product,sumofno = int(l1[0]),int(l1[0])
        for i in range(len(l1)-1):
            product = product * int(l1[i+1])
            sumofno += int(l1[i+1])
        result = product - sumofno
        return result

n = 4421
a = Solution.subtractProductAndSum(n)
print(a)