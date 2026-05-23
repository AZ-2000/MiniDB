class Node:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def get_height(self, node):
        if node:
            return node.height
        else:
            return 0
        
    def get_balance(self, node):
        if node:
            return self.get_height(node.left) - self.get_height(node.right)
        else:
            return 0
        
    def right_rotate(self, z):
        y = z.left
        T3 = z.right
        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def left_rotate(self, z):
        y = z.right
        T3 = z.left
        y.left = z
        z.right = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, key, value):
        if not root:
            return Node(key, value)
        if key < root.key:
            root.left = self.insert(root.left, key, value)
        elif key > root.key:
            root.right = self.insert(root.right, key, value)
        else:
            print("Duplicate key found!")
            return
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            if key >root.left.key:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            if key < root.right.key:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root


    def get_min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current
    
    def delete(self, root, key):
        if root is None:
            return 
        else:
            if key < root.key:
                root.left = self.delete(root.left, key)
            elif key > root.key:
                root.right = self.delete(root.right, key)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left

                successor = self.get_min_value_node(root.right)
                root.key = successor.key
                root.value = successor.value
                root.right = self.delete(root.right, successor.key)
            if root is None:
                return 
            root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
            balance = self.get_balance(root)
            if balance > 1:
                if self.get_balance(root.left) >= 0:
                    return self.right_rotate(root)
                else:
                    root.left = self.left_rotate(root.left)
                    return self.right_rotate(root)
            if balance < -1:
                if self.get_balance(root.right) >= 0:
                    return self.left_rotate(root)
                else:
                    root.right = self.right_rotate(root.right)
                    return self.left_rotate(root)
            return root


    def inorder(self, root):
        if not root:
            return 
        else:
            self.inorder(root.left)
            print(root.key, end = " ")
            self.inorder(root.right)
    
    def search(self, root, key):
        if root is None:
            return 
        else:
            if root.key == key:
                return root
            if key < root.key:
                return self.search(root.left,key)
            if key > root.key:
                return self.search(root.right, key)