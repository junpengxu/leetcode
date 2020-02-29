class Solution:
    def romanToInt(self, s: str) -> int:
        auxiliary_dict = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

        auxiliary_list = list(auxiliary_dict.keys())

        res = 0
        while True:
            for item in auxiliary_list:
                if s.startswith(item):
                    res += auxiliary_dict[item]
                    s = s[len(item):]
                    break
                if not s:
                    return res


assert Solution().romanToInt('MMMCMXCIX') == 3999
assert Solution().romanToInt('MCMXCIV') == 1994
assert Solution().romanToInt('I') == 1
