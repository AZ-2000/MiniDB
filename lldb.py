from linkedlist import LinkedList

class LinkedListDatabase:

    def __init__(self):
        self.tables = {}

    def create_table(self, name):
        if name in self.tables:
            return

        linked_list = LinkedList()
        linked_list.root = None

        self.tables[name] = linked_list


    def insert(self, table, key, value):

        if table not in self.tables:
            return

        linked = self.tables[table]

        # Check duplicate
        if linked.search(linked.root, key):
            return

        linked.root = linked.insert(
            linked.root,
            key,
            value
        )


    def select(self, table, key):

        if table not in self.tables:
            return None

        linked = self.tables[table]

        node = linked.search(
            linked.root,
            key
        )

        if node:
            return node.value

        return None


    def update(self, table, key, value):

        if table not in self.tables:
            return

        linked = self.tables[table]

        node = linked.search(
            linked.root,
            key
        )

        if node:
            node.value = value


    def delete(self, table, key):

        if table not in self.tables:
            return

        linked = self.tables[table]

        linked.root = linked.delete(
            linked.root,
            key
        )