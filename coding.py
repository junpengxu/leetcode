class Solution:
    def myAtoi(self, str: str) -> int:

        # 1. 判断输入的边界条件
        if not str:
            return 0
        # 判断全空格
        elif not str.lstrip():
            return 0

        if len(str) == 1:
            if str.isdigit():
                return str
            else:
                return 0
        flag = 1
        res = 0
        # 2. 去除空格
        str = str.lstrip()
        str = str.rstrip()

        if '-' == str[0]:
            str = str[1:]
            flag = 0
        elif '+' == str[0]:
            str = str[1:]

        if str[0].isdigit():
            for i in str:
                if i.isdigit():
                    res *= 10
                    res += int(i)
                    if res > 2 ** 31:
                        return 2 ** 31 if flag else - 2 ** 31
                else:
                    return res if flag else -res
        else:
            return 0

        return res if flag else -res


#
assert Solution().myAtoi("+42") == 42
assert Solution().myAtoi("       ") == 0
assert Solution().myAtoi("-") == 0
assert Solution().myAtoi("  -42") == -42
assert Solution().myAtoi("- 42") == 0
assert Solution().myAtoi(" -422ff") == -422
assert Solution().myAtoi(" -4220  ff") == -4220
assert Solution().myAtoi(" -4220 21ff") == -4220
assert Solution().myAtoi("-91283472332") == -2147483648
assert Solution().myAtoi("+1") == 1
assert Solution().myAtoi("+12") == 12
assert Solution().myAtoi("+1  ") == 1
assert Solution().myAtoi("    +1") == 1
assert Solution().myAtoi("+  21") == 0
assert Solution().myAtoi("  -0012a42") == -12
