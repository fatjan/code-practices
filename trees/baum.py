class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    # insert into tree
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    # print tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
    
    # inorder traversal
    # Left -> Root -> Right
    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            res += self.inorder_traversal(root.right)
        return res
    
    # preorder traversal
    # Root -> Left -> Right
    def preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res += root.preorder_traversal(root.left)
            res += root.preorder_traversal(root.right)
        return res
    
    # postorder traversal
    # Left -> Right -> Root
    def postorder_traversal(self, root):
        res = []
        if root:
            res = self.postorder_traversal(root.left)
            res += self.postorder_traversal(root.right)
            res.append(root.data)
        return res


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print('this is the tree')
root.print_tree()
print('this is the inorder traversal tree')
print(root.inorder_traversal(root))
print('this is the preorder traversal tree')
print(root.preorder_traversal(root))
print('this is the post-order traversal tree')
print(root.postorder_traversal(root))




