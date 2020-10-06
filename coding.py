class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)  # 字符串的长
        # dp = [[False] * n for _ in range(n)]#构建一个矩阵，初始值全部为False
        line = [False] * n  # 只需要存储dp[i][j]前一列的值就可以计算dp[i][j]的状态
        ans = ""  # 记录最长回文字串
        # 枚举子串的长度 l+1
        for j in range(0, n):
            for i in range(0, j + 1):
                if j == i:
                    line[i] = True
                elif j - i == 1:
                    line[i] = (s[i] == s[j])
                else:
                    line[i] = (line[i + 1] and s[i] == s[j])
                if line[i] and j - i + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans


if __name__ == '__main__':
    A = Solution()
    # print(A.longestPalindrome("babad"))
    # print(A.longestPalindrome("cbbd"))
    print(A.longestPalindrome("aaaacabdkacaa"))
    # print(A.longestPalindrome("aaaaaa"))
