# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def helper(root, target):
            """
            return : list  ,the index from root node to taget node
            """
            ret = list()

            while root != target:
                if root.val < target.val:
                    ret.append(root)
                    root = root.right
                else:
                    ret.append(root)
                    root = root.left
            ret.append(target)
            return ret
        f_list = helper(root, p)
        s_list = helper(root, q)

        s_target = list()
        for item in f_list:
            if item in s_list:
                s_target.append(item)
        return s_target[-1]


if __name__ == "__main__":
    s = Solution()

    node0 = TreeNode(2)
    node1 = TreeNode(1)
    node2 = TreeNode(4)
    node3 = None
    node4 = None
    node5 = TreeNode(3)
    node6 = TreeNode(5)

    node0.left = node1
    node0.right = node2
    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.right = node6
    node5.left = None
    node5.right = None
    node6.left = None
    node6.right = None

    print(s.lowestCommonAncestor(node0, node5, node6).val)
