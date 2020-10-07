class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        flag = -1 if x < 0 else 1
        x = x if x > 0 else -x
        while x != 0:
            tmp = x % 10
            if res > (2 << 30) // 10 or (res == (2 << 30) // 10 and tmp > 7):
                return 0
            if res < - (2 << 30) // 10 or (res == - (2 << 30) // 10 and tmp < -8):
                return 0
            res = res * 10 + tmp
            x //= 10
        return res * flag


if __name__ == '__main__':
    A = Solution()
    print(A.reverse(1534236469))
