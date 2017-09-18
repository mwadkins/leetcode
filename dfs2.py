class TreeNode () :
    def __init__(self,v):
        self.val=v
        self.left=None
        self.right=None
    

def preorder (node):
    if (node != None):
        print node.val," ",
        preorder (node.left)
        preorder (node.right)
        
def inorder (node):
    if (node != None):
        inorder (node.left)
        print node.val," ",
        inorder (node.right)

def postorder (node):
    if (node != None):
        postorder (node.left)
        postorder (node.right)
        print node.val," ",

def inorderIterative (node):
    if (node==None):
        return
    stack = []
    curr=node
    while ((curr!=None) or (len(stack))):
        while (curr!=None):
            stack.append(curr)
            curr=curr.left
            
        curr=stack.pop()
        print curr.val," ",
        
        curr=curr.right
        

root=TreeNode (1)
root.left = TreeNode (2)
root.right = TreeNode (3)
root.left.left = TreeNode (4)
root.left.right = TreeNode (5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)

print "preorder "
preorder(root)
print " "

print "inorder "
inorder(root)

print " "
print "postorder "
postorder(root)

print " "
print "inorderIterative "
inorderIterative(root)
print " "
