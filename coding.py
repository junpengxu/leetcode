class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        else:
            new_s = s.rstrip().split()
            if not new_s:
                return 0
            return len(new_s[-1])

if __name__ == '__main__':
    A = Solution()
    print(A.lengthOfLastWord('     '))
    print(A.lengthOfLastWord(' a  a  '))
    print(A.lengthOfLastWord(' a    '))