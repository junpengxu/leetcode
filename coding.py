from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        res_dict = defaultdict(list)
        for item in strs:
            tmp_str = ''.join(sorted(list(item)))
            if tmp_str not in res_dict:
                res_dict[tmp_str] = [item]
            else:
                res_dict[tmp_str].append(item)
        return list(res_dict.values())


if __name__ == '__main__':
    A = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(A.groupAnagrams(strs))
