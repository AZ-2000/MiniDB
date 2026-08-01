from AVL import AVLTree
from LRU import LRUCache
from storage import Storage
import threading
import copy

class Database:
    """MiniDB using AVL trees per table + LRU cache."""

    def __init__(self, cache_capacity=5):
        """Initialise tables and LRU cache."""
        self.tables = {}
        self.cache = LRUCache(cache_capacity)
        self.storage = Storage()
        self.lock = threading.RLock()
        self.snapshot = None
        self.in_transaction = False
        self.cache_snapshot = None
        self.load_database()

    def begin(self):

        if self.in_transaction:
            print("Transaction already active")
            return

        self.lock.acquire()

        self.snapshot = copy.deepcopy(self.tables)
        self.cache_snapshot = copy.deepcopy(self.cache)

        self.in_transaction = True

        print("Transaction started")


    def commit(self):

        if not self.in_transaction:
            print("No active transaction")
            return

        try:
            self.storage.save(self.tables)

            self.snapshot = None
            self.cache_snapshot = None
            self.in_transaction = False

            print("Transaction committed")

        except Exception as e:
            print("Commit failed:", e)

            self.tables = self.snapshot
            self.cache = self.cache_snapshot

            self.snapshot = None
            self.cache_snapshot = None
            self.in_transaction = False

            print("Transaction rolled back")

        finally:
            self.lock.release()

    def rollback(self):

        if not self.in_transaction:
            print("No active transaction")
            return

        self.tables = self.snapshot
        self.cache = self.cache_snapshot

        self.snapshot = None
        self.cache_snapshot = None

        self.in_transaction = False

        self.lock.release()

        print("Transaction rolled back")



    def load_database(self):

        data = self.storage.load()

        for table_name, records in data.items():

            self.create_table(table_name, save = False)

            for record in records:

                self.insert(
                    table_name,
                    record["key"],
                    record["value"],
                    save = False, 
                    cache = False
                )

    def helper(self, node):
        """In-order traversal printer for AVL tree."""
        if node is None:
            return

        self.helper(node.left)
        print(f"ID: {node.key} | Student Data: {node.value}")
        self.helper(node.right)

    def show_table(self, table):
        with self.lock:
            """Print all records in a table."""
            if table not in self.tables:
                print("Table does not exist")
                return

            tree = self.tables[table]

            print(f"\n--- Table: {table} ---")
            self.helper(tree.root)
            print("\n----------------------")

    def create_table(self, name, save = True):
        with self.lock:
            """Create a new empty table."""
            if name in self.tables:
                print("Table already exists")
                return

            tree = AVLTree()
            tree.root = None
            self.tables[name] = tree
            if save and not self.in_transaction:
                self.storage.save(self.tables)


            print(f"Table '{name}' created")

    def insert(self, table, key, value, save = True, cache = True):
        """Insert a record into a table."""
        with self.lock:
            if table not in self.tables:
                print("Table does not exist")
                return

            tree = self.tables[table]

            if tree.search(tree.root, key):
                print("Duplicate key found!")
            else:
                tree.root = tree.insert(tree.root, key, value)
                if save and not self.in_transaction:
                    self.storage.save(self.tables)
                if cache:
                    self.cache.put((table, key), value)
                # print("CACHE: ", self.cache.hashmap)
                # print("Inserted")

    def select(self, table, key):
        with self.lock:
            """Retrieve a record (uses cache if available)."""
            if table not in self.tables:
                print("Table does not exist")
                return None

            cache_key = (table, key)

            cached = self.cache.get(cache_key)
            if cached != -1:
                # print("CACHE HIT")
                return cached

            tree = self.tables[table]
            node = tree.search(tree.root, key)

            if node:
                self.cache.put(cache_key, node.value)
                return node.value

            return None

    def update(self, table, key, value):
        """Update a record in a table."""
        with self.lock:
            if table not in self.tables:
                print("Table does not exist")
                return

            tree = self.tables[table]
            node = tree.search(tree.root, key)

            if node:
                node.value = value
                self.cache.put((table, key), value)
                if not self.in_transaction:
                    self.storage.save(self.tables)
                print("Updated")
            else:
                print("Record not found")

    def delete(self, table, key):
        """Delete a record from a table."""
        with self.lock:
            if table not in self.tables:
                print("Table does not exist")
                return

            tree = self.tables[table]
            tree.root = tree.delete(tree.root, key)
            if not self.in_transaction:
                self.storage.save(self.tables)


            try:
                del self.cache.hashmap[(table, key)]
            except KeyError:
                pass

            print("Deleted")

    def show_tables(self):
        with self.lock:
            """List all tables."""
            if not self.tables:
                print("No tables created")
                return

            print("Tables:")
            for name in self.tables:
                print("-", name)