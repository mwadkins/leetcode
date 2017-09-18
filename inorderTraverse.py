# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def traverse (self,node,ret):
        if (node):
		self.traverse(node.left,ret)
		ret.append(node.val)
            	self.traverse(node.right,ret)
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret=[]
        self.traverse(root,ret)
        return ret


t = TreeNode(1)
t.right=TreeNode(2)
t.right.left=TreeNode(3)

sol=Solution()
r=sol.inorderTraversal(t)
print r
