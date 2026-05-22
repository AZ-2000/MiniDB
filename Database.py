from AVL import AVLTree
from LRU import LRUCache

class Database:

    def __init__(self, cache_capacity=5):

        self.tree = AVLTree()
        self.root = None

        self.cache = LRUCache(cache_capacity)
    
    def insert(self, key, value):

        self.root = self.tree.insert(
            self.root,
            key,
            value
        )

        self.cache.put(key, value)

        print("Inserted")
    
    def select(self, key):

        cached = self.cache.get(key)

        if cached != -1:
            print("CACHE HIT")
            return cached

        node = self.tree.search(self.root, key)

        if node:
            self.cache.put(key, node.value)
            return node.value

        return None
    def update(self, key, new_value):

        node = self.tree.search(self.root, key)

        if node:
            node.value = new_value
            self.cache.put(key, new_value)
            print("Updated")

        else:
            print("Record not found")
    
    def delete(self, key):

        node = self.tree.search(self.root, key)

        if node:

            self.root = self.tree.delete(
                self.root,
                key
            )

            print("Deleted")

        else:
            print("Record not found")