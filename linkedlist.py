class Node:
    def __init__(self, key, value = None, next = None):
        self.key = key
        self.value = value
        self.next = next

class LinkedList:

    def insert(self,root,key,value):
        new_node = Node(key, value)

        if root is None:
            root = new_node
        else:
            current = root
            new_node.next = current
            root = new_node
        return root
    
    def get_min_val(self, root):
        if root is None:
            return None
        minimum = root
        current = root.next
        while current:
            if current.key < minimum.key:
                minimum = current
            current = current.next
        return minimum

    def delete(self, root, key):
        current = root
        previous = None

        while current is not None:
            if current.key == key:
                if previous is None:
                    root = current.next
                else:
                    previous.next = current.next

                return root

            previous = current
            current = current.next

        return root

    def inorder(self, root):
        current = root
        while current:
            print(current.key, end = " ")
            current = current.next

    def search(self, root, key):
        current = root
        while current:
            if current.key == key:
                return current
            else:
                current = current.next
        return None

