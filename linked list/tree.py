class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

     def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res
    
     def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def postorder(root):
            if root is None:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        postorder(root)
        return res
     def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def preorder(root):
            if root is None:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
            
        preorder(root)
        return res
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(root.inorderTraversal(root))
print(root.postorderTraversal(root))
print(root.preorderTraversal(root))


'''
inorder

res =[]
stack = []
cur = root
while cur or stack:
    while cur:
        stack.append(cur)
        cur = cur.left
    cur = stack.pop()
    res.append(cur)
    cur = cur.right
    
return res
'''

'''
 preorder
 
res =[]
stack = []
if root is None:
   return res

stack.append(root)
while stack:
    node = stack.pop()
    res.append(node.val)
    if node.right is not None:
      stack.append(node.right)
    if node.left is not None:
      stack.append(node.left)
return res
'''


'''
     postorder
        res =[]
        stack = []
        if root is None:
          return res

        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        res.reverse()
        return res    

'''

'''
def checkBST(root):
    if root == None or (root.left == None and root.right == None):
        return True

    elif root.right == None:
        return root.left.data < root.data and checkBST(root.left)

    elif root.left == None:
        return root.right.data >= root.data and checkBST(root.right)

    return checkBST(root.left) and checkBST(root.right)



'''