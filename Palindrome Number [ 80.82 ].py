# LEETCODE 

class Solution:
    def isPalindrome(x: int) -> bool:
        y = str(x)
        new_list = list(y)
        no = new_list[::-1]
        new_no = "".join(no)
        if y == new_no:
            return True
        else:
            return False

a = Solution.isPalindrome(121)
print(a)