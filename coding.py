class Solution:
    def intToRoman(self, num: int) -> str:
        auxiliary_dict = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM',
            4: 'IV',
            9: 'IX'
        }
        auxiliary_list = list(auxiliary_dict.keys())
        auxiliary_list.sort(reverse=True)

        res = ''
        while num:
            for item in auxiliary_list:
                if item <= num:
                    res += auxiliary_dict[item]
                    num -= item
                    break

        return res


assert Solution().intToRoman(1) == 'I'
assert Solution().intToRoman(3) == 'III'
assert Solution().intToRoman(4) == 'IV'
assert Solution().intToRoman(9) == 'IX'
assert Solution().intToRoman(58) == 'LVIII'
assert Solution().intToRoman(1994) == 'MCMXCIV'
assert Solution().intToRoman(3999) == 'MMMCMXCIX'
