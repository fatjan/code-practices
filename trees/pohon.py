class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # insert to tree
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

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    # Inorder traversal
    # Left -> Root -> Right
    def InorderTraversal(self, root):
        res = []
        if root:
            res = self.InorderTraversal(root.left)
            res.append(root.data)
            res = res + self.InorderTraversal(root.right)
        return res

    # Preorder traversal
    # Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
    
    # Post-order traversal
    # Left -> Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
            res.append(root.data)
        return res

# Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.PrintTree()


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print('this is the tree')
root.PrintTree()
print('this is the inorder traversal tree')
print(root.InorderTraversal(root))
print('this is the preorder traversal tree')
print(root.PreorderTraversal(root))
print('this is the post-order traversal tree')
print(root.PostorderTraversal(root))
