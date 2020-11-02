class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
                   'V': 5, 'IV': 4, 'I': 1}

        def recurse(s, index, res):
            if index >= len(s):
                return res
            if s[index:index + 2] in mapping:
                return recurse(s, index + 2, res + mapping[s[index:index + 2]])
            else:
                return recurse(s, index + 1, res + mapping[s[index:index + 1]])

        return recurse(s, 0, 0)


if __name__ == '__main__':
    A = Solution()
    print(A.romanToInt("III"))
