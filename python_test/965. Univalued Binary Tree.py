# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        pass

if __name__ == '__main__':
    root = [1,1,1,1,1,None,1]
    Solution().isUnivalTree(root)