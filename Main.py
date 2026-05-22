from Database import Database

def show_help():
    print("""
**************************************************
*                MINI DATABASE CLI               *
**************************************************

USAGE:

1. CREATE TABLE <table_name>
   e.g. CREATE TABLE users

2. INSERT <table> <key> <name> <age>
   e.g. INSERT users 1 Alice 20

3. SELECT <table> <key>
   e.g. SELECT users 1

4. UPDATE <table> <key> <name> <age>
   e.g. UPDATE users 1 Alice 21

5. DELETE <table> <key>
   e.g. DELETE users 1

6. SHOW TABLES
   e.g. SHOW TABLES

7. SHOW TABLE <table_name>
   e.g. SHOW TABLE patient

8. HELP

9. EXIT

**************************************************
""")
    
db = Database()
show_help()

while True:

    command = input("db > ").strip()
    parts = command.split()

    if len(parts) == 0:
        continue

    cmd = parts[0].upper()

    if cmd == "CREATE" and len(parts) >= 3 and parts[1].upper() == "TABLE":
        table = parts[2]
        db.create_table(table)

    elif parts[0] == "INSERT":

        table = parts[1]
        key = int(parts[2])

        age = int(parts[-1])
        name = " ".join(parts[3:-1])

        db.insert(
            table,
            key,
            {
                "name": name,
                "age": age
            }
        )

    elif cmd == "SELECT":
        if len(parts) < 3:
            print("Usage: SELECT <table> <key>")
            continue

        table = parts[1]
        key = int(parts[2])

        result = db.select(table, key)
        print(result)

    elif parts[0] == "UPDATE":

        table = parts[1]
        key = int(parts[2])

        age = int(parts[-1])
        name = " ".join(parts[3:-1])

        db.update(
            table,
            key,
            {
                "name": name,
                "age": age
            }
        )
    elif parts[0] == "SHOW" and parts[1] == "TABLE":

        table = parts[2]
        db.show_table(table)

    elif cmd == "DELETE":
        if len(parts) < 3:
            print("Usage: DELETE <table> <key>")
            continue

        table = parts[1]
        key = int(parts[2])

        db.delete(table, key)

    elif cmd == "SHOW":
        if len(parts) >= 2 and parts[1].upper() == "TABLES":
            db.show_tables()
        else:
            print("Usage: SHOW TABLES")

    elif cmd == "HELP":
        show_help()

    elif cmd == "EXIT":
        print("Shutting down database...")
        break

    else:
        print("Unknown command. Type HELP for usage.")