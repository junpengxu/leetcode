class Solution:
    def merge(self, intervals):
        new_list = []
        new_list.append(intervals[0][0])
        for item in intervals:
            for i in item:
                if i > new_list[-1]:
                    new_list.append(i)

        for i in range(0, len(new_list), 2):
            pass


if __name__ == '__main__':
    A = Solution()
    A.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
