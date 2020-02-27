class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if -1 << 31 >= x or x > 1 << 30 -1:
            return 0
        elif x > 0:
            flag = 1
        else:
            flag = 0
            x = -x

        # 去掉末尾的0
        while x:
            if x % 10:
                break
            x = x // 10

        while x:
            res = res * 10
            res += x % 10
            x = x // 10

        return res if flag else -res


Solution().reverse(1534236469)
assert Solution().reverse(-123) == -321
assert Solution().reverse(1230) == 321
assert Solution().reverse(101) == 101
