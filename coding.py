from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return (all(A[i] >= A[i + 1] for i in range(len(A) - 1)) or all(A[i] <= A[i + 1] for i in range(len(A) - 1)))


if __name__ == '__main__':
    A = Solution()
    print(A.isMonotonic([1, 1, 1]))
    print(A.isMonotonic([1, 0, 1]))
    print(A.isMonotonic([1, 1, 0, 1]))
    print(A.isMonotonic([0, 0, 1]))
    print(A.isMonotonic([1, 3, 2]))
    print(A.isMonotonic([1, 1, 1]))
    print(A.isMonotonic([0, 0, 0]))
    print(A.isMonotonic([1, 2, 2, 3]))
    print(A.isMonotonic([6, 5, 4, 4]))
    print(A.isMonotonic([11, 11, 9, 4, 3, 3, 3, 1, -1, -1, 3, 3, 3, 5, 5, 5]))
