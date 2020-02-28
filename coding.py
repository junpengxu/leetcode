class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_x = x
        res = 0
        while x:
            res = res * 10 + x % 10
            x = x // 10
        return x_x == res
