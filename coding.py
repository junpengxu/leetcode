class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)  # 字符串的长
        dp = [[False] * n for _ in range(n)]  # 构建一个矩阵，初始值全部为False
        ans = ""
        for j in range(n):  # 列
            for i in range(j, -1, -1):  # 行
                print(s[i:j])
                if i == j:
                    dp[i][j] = True
                elif j - i == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and j - i + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans
# 最后一次的遍历记录
# a
# ca
# aca
# kaca
# dkaca
# bdkaca
# abdkaca
# cabdkaca
# acabdkaca
# aacabdkaca
# aaacabdkaca
# aaaacabdkaca
if __name__ == '__main__':
    A = Solution()
    # print(A.longestPalindrome("babad"))
    # print(A.longestPalindrome("cbbd"))
    print(A.longestPalindrome("aaaacabdkacaa"))
    # print(A.longestPalindrome("aaaaaa"))
