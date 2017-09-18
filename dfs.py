class TreeNode(object):
    def __init__ (self,x):
        self.val = x
        self.left=None
        self.right=None

def postorderTraversal (root):
    if (root==None):
        return
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print root.val," ",
    
def preorderTraversal (root):
    if (root==None):
        return
    print root.val," ",
    preorderTraversal(root.left)
    preorderTraversal(root.right)
    
def inorderTraversal (root):
    if (root==None):
        return
    inorderTraversal(root.left)
    print root.val," ",
    inorderTraversal(root.right)

def preorderTraversalIterative (root):
    stack = []
    stack.append(root)
    while (len(stack)>0):
        node=stack.pop()
        print node.val," ",
        if (node.right!=None):
            stack.append(node.right)
        if (node.left!=None):
            stack.append(node.left)
   
def inorderTraversalIterative (root):
    stack = []
    curr=root
    while ((curr!=None) or (len(stack)>0)):
        while (curr!=None):
            stack.append(curr)
            curr=curr.left
        node=stack.pop()
        print node.val," ",
        curr=node.right


def bfsIterative (root):
    queue=[]
    queue.append(root)
    
    while (len(queue)>0):
        # pop is a misnomer here, this is really a dequeue
        curr=queue.pop(0)
        if (curr.left != None):
            queue.append(curr.left)
        if (curr.right != None):
            queue.append(curr.right)
        print curr.val," ",
    
root=TreeNode (1)
root.left = TreeNode (2)
root.right = TreeNode (3)
root.left.left = TreeNode (4)
root.left.right = TreeNode (5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)

print "inorder "
inorderTraversal(root)

print " "
print "preorder "
preorderTraversal(root)

print " "
print "postorder "
postorderTraversal(root)

print " "
print "inorder iterative"
inorderTraversalIterative(root)

print " "
print "preorder iterative"
preorderTraversalIterative(root)

print " "
print "postorder iterative (hard, not done yet"

print " "
print "bfs iterative"
bfsIterative(root)
