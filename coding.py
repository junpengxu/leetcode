from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        max_prefix = strs[0]
        for str in strs:
            if not max_prefix:
                return ""
            else:
                max_prefix = self.get_max_prefix(max_prefix, str)
        return max_prefix

    @staticmethod
    def get_max_prefix(str_1, str_2):
        res = []
        for s_1, s_2 in zip(str_1, str_2):
            if s_1 == s_2:
                res.append(s_1)
            else:
                break
        return "".join(res)


if __name__ == '__main__':
    A = Solution()
    print(A.longestCommonPrefix(["abc", "aba"]))
    print(A.longestCommonPrefix(["cir", "car"]))
