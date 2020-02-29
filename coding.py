class Solution:
    def longestCommonPrefix(self, strs):

        if not strs:
            return ''

        # 找到最短的。 最长前缀一定小于最短的
        min_len_str = strs[0]
        for item in strs[1:]:
            if len(min_len_str) >= len(item):
                min_len_str = item

        for i in range(0, len(min_len_str)+1):
            new_strs = [item[:i] for item in strs]
            if len(set(new_strs)) != 1:
                return min_len_str[:i - 1]
        return min_len_str

assert Solution().longestCommonPrefix(["aa", "ab"]) == 'a'

assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ''
assert Solution().longestCommonPrefix(["a", "b"]) == ''
assert Solution().longestCommonPrefix(["aa", "ab"]) == 'a'
assert Solution().longestCommonPrefix(["a", "a"]) == 'a'
assert Solution().longestCommonPrefix([]) == ''
assert Solution().longestCommonPrefix([""]) == ''
assert Solution().longestCommonPrefix(["a"]) == 'a'
