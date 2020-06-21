from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()
        res = [intervals[0]]
        for item in range(1, len(intervals)):
            if intervals[item][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[item][1])
            else:
                res.append(intervals[item])
        return res


if __name__ == '__main__':
    A = Solution()
    print(A.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(A.merge([[1, 3], [2, 6], [0, 10], [15, 18]]))
    print(A.merge([[1, 4], [4, 6]]))
    print(A.merge([[1, 4], [0, 6]]))
    print(A.merge([[1, 4], [0, 2]]))
