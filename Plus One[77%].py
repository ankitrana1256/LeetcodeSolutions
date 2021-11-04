class Solution:
    def plusOne(digits):
        res = list(str(int("".join(map(str, digits))) + 1))
        digits = list(map(int,res))
        return digits
    
digits = [9, 9]
# digits = [1,2,0]
a = Solution.plusOne(digits)
print(a)