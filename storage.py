import json
import os

class Storage:

    def __init__(self, filename="database.json"):
        self.filename = filename

    def save(self, tables):

        data = {}

        for table_name, tree in tables.items():

            records = []

            self.collect_records(tree.root, records)

            data[table_name] = records

        temp_file = self.filename + ".tmp"

        with open(temp_file, "w") as file:
            json.dump(data, file, indent=4)
            file.flush()
            os.fsync(file.fileno())

        os.replace(temp_file, self.filename)


    def collect_records(self, node, records):

        if node is None:
            return

        self.collect_records(node.left, records)

        records.append({
            "key": node.key,
            "value": node.value
        })

        self.collect_records(node.right, records)


    def load(self):

        if not os.path.exists(self.filename):
            return {}

        try:
            with open(self.filename, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            print("Database file is corrupted.")
            return {}