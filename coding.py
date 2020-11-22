# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        stack = []
        res = []
        tmp = root
        while stack or tmp:
            if tmp:
                stack.append(tmp)
                tmp = tmp.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                tmp = tmp.right
        return res


if __name__ == '__main__':
    A = Solution()
    A.inorderTraversal()
