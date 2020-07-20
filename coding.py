class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        if s[0] == "0":
            return 0
        size = len(s)
        dp = [0 for _ in range(size + 1)]
        dp[0], dp[1] = 1, 1

        # dp[i-1] 表示选择一个（连续两个数字）
        # dp[i] 表示选择两个（将前面的数，与自己，分别当作两个数字）
        for i in range(1, size):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i + 1] = dp[i - 1]
                else:
                    return 0
            else:
                if s[i-1] == '1' or (s[i-1] == '2' and "1" <= s[i] <= "6"):
                    dp[i + 1] = dp[i - 1] + dp[i]
                else:
                    dp[i + 1] = dp[i]

        return dp[-1]


if __name__ == '__main__':
    A = Solution()
    print(A.numDecodings("1234"))
