class Solution:
    def myPow(self, x: float, n: int) -> float:

        def divide_conquer(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            elif n % 2 == 0:
                return divide_conquer(x * x, n // 2)
            else:
                return x * divide_conquer(x * x, n // 2)

        if n > 0:
            return divide_conquer(x, n)
        else:
            return 1 / divide_conquer(x, -n)


if __name__ == '__main__':
    A = Solution()
    print(A.myPow(2.00000, -2))
