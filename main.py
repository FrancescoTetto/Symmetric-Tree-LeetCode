class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True #An empty root is symetric

        def isMirror(left, right):
            if not left and not right:
                return True # Because both nodes are empty, they are symetric
            if not left or not right:
                return False
            
            return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)

        return isMirror(root.left, root.right)



root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(4), TreeNode(3))

solution = Solution()
print(solution.isSymmetric(root))
       
