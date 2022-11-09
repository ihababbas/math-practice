class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def areMirror(a, b):
    list1= [] # 3 1
    list2= []
    def inorder1(a):
        if a is None:
            return 
        inorder1(a.left)
        list1.append(a.val)
        inorder1(a.right)
        
    
    def inorder2(b):
        if b is None:
            return 
        inorder2(b.left)
        list2.append(b.val) 
        inorder2(b.right)
        
    inorder1(a)
    inorder2(b)
    list2.reverse()
    if len(list1) != len(list2):
        return False 
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            pass       
        else:
            return False
    return True
    
root1 = Node(1)
root2 = Node(1)
root1.left=  Node(2)
root2.right= Node(2)


root1.left.right=  Node(3)
root2.right.left= Node(3)



print(areMirror(root1,root2))
    


   
        
        
        
        
        

   

   


  
