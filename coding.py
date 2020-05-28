class Solution:
    def plusOne(self, digits):
        flag = 1
        for index in range(len(digits) - 1, -1, -1):
            if digits[index] + flag == 10:
                digits[index] = 0
                flag = 1
                if index == 0:
                    digits.insert(0, 1)
                    return digits
            elif flag == 1:
                digits[index] += flag
                flag = 0
            else:
                return digits
        return digits


if __name__ == '__main__':
    A = Solution()
    print(A.plusOne([1,2,3]))
    print(A.plusOne([1]))
    print(A.plusOne([9, 9, 9]))
    print(A.plusOne([9, 9, 0]))
    print(A.plusOne([1, 9, 9]))
