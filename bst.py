class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
        
        
class BST:
    def __init__(self,value):
        self.root = Node(value)
        
    def insert(self,root,newnode):
        
        if root.value > newnode.value:
            if root.left is None:     
                root.left = newnode
            else:              
                self.insert(root.left,newnode)
                    
        else:
            if root.right is None:
                root.right = newnode
                    
            else :
                self.insert(root.right,newnode) 
                    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.value,end=' ')
            self.inorder(root.right)
                
    def preorder(self,root):
        if root:
            print(root.value, end = ' ')
            self.preorder(root.left)
            self.preorder(root.right)
                
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value,end=' ')          
        
        
        
        
b =  BST(5)

b.insert(b.root, Node(8))
b.insert(b.root, Node(10))
b.insert(b.root, Node(3))
b.insert(b.root, Node(1))
b.insert(b.root, Node(6))
b.insert(b.root, Node(4))
b.insert(b.root, Node(7))
b.insert(b.root, Node(9))
b.insert(b.root, Node(12))


# b.preorder(b.root)
b.inorder(b.root)
# b.postorder(b.root)

