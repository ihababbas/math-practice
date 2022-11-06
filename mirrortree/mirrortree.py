class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def areMirror(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.val != b.val:
        return False
    if a.left is not None and b.right is not None:
        if a.left.val != b.right.val:
            return False
        else: 
            areMirror(a.left,b.right)
    if a.right is not None and b.left is not None:
        if a.right.val != b.left.val:
            return False
        else: 
            areMirror(a.right,b.left)
    
    return True
    

root1 = Node(1)
root2 = Node(1)
root1.left=  Node(2)
root2.right= Node(2)
root1.left.right=  Node(3)
root2.right.left= Node(3)


print(areMirror(root1,root2))