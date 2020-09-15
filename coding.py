class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        len_s1 = len(s1)
        len_s2 = len(s2)
        for i in range(0, len_s2 - len_s1 + 1):
            if Counter(s2[i:i + len_s1]) == Counter(s1):
                return True
        return False


if __name__ == '__main__':
    A = Solution()
    print(A.checkInclusion("ayb", "eidbaooo"))
