from AVL import AVLTree
from LRU import LRUCache


class Database:

    def __init__(self, cache_capacity=5):
        self.tables = {}
        self.cache = LRUCache(cache_capacity)
    def _inorder(self, node):

        if node is None:
            return
        
        self._inorder(node.left)

        print(f"ID: {node.key} | Data: {node.value}")

        self._inorder(node.right)
        
    def show_table(self, table):

        if table not in self.tables:
            print("Table does not exist")
            return

        tree = self.tables[table]

        print(f"\n--- Table: {table} ---")

        self._inorder(tree.root)

    print("\n----------------------")
    def create_table(self, name):

        if name in self.tables:
            print("Table already exists")
            return

        tree = AVLTree()
        tree.root = None

        self.tables[name] = tree

        print(f"Table '{name}' created")

    def insert(self, table, key, value):

        if table not in self.tables:
            print("Table does not exist")
            return

        tree = self.tables[table]
        if tree.search(tree.root, key) is not None:
            print("Error: Duplicate key")
            return

        tree.root = tree.insert(tree.root, key, value)

        self.cache.put((table, key), value)

        print("Inserted")

    def select(self, table, key):

        if table not in self.tables:
            print("Table does not exist")
            return None

        cache_key = (table, key)

        cached = self.cache.get(cache_key)
        if cached != -1:
            print("CACHE HIT")
            return cached

        tree = self.tables[table]

        node = tree.search(tree.root, key)

        if node:
            self.cache.put(cache_key, node.value)
            return node.value

        return None

    def update(self, table, key, value):

        if table not in self.tables:
            print("Table does not exist")
            return

        tree = self.tables[table]

        node = tree.search(tree.root, key)

        if node:
            node.value = value

            self.cache.put((table, key), value)

            print("Updated")
        else:
            print("Record not found")

    def delete(self, table, key):

        if table not in self.tables:
            print("Table does not exist")
            return

        tree = self.tables[table]

        tree.root = tree.delete(tree.root, key)

        try:
            del self.cache.hashmap[(table, key)]
        except KeyError:
            pass

        print("Deleted")

    def show_tables(self):

        if not self.tables:
            print("No tables created")
            return

        print("Tables:")

        for name in self.tables:
            print("-", name)