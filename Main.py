from Database import Database

def show_help():
    print("""
USAGE:

1. CREATE TABLE <table_name>
   e.g. CREATE TABLE students

2. INSERT <table> <Student ID> <First Name> <Last Name> <age> <semester> <WAM> <Grade>
   e.g. INSERT students 1 Alice 20 1 75.5 HD

3. SELECT <table> <Student ID>
   e.g. SELECT students 1

4. UPDATE <table> <Student ID> <First Name> <Last Name> <age> <semester> <WAM> <Grade>
   e.g. UPDATE students 1 Alice 21 2 80.0 D

5. DELETE <table> <Student ID>
   e.g. DELETE students 1

6. SHOW TABLES
   e.g. SHOW TABLES

7. SHOW TABLE <table_name>
   e.g. SHOW TABLE students

8. HELP

9. EXIT
""")
    
db = Database()
show_help()
allowed_grades = {"HD", "D", "C", "P", "F"}
while True:

    command = input("MINIDB COMMAND > ").strip()
    parts = command.split()

    if len(parts) == 0:
        continue

    cmd = parts[0].upper()

    if cmd == "CREATE":
        if len(parts) == 3 and parts[1].upper() == "TABLE":
            table = parts[2]
            db.create_table(table)
        else:
            print("Usage: CREATE TABLE <table_name>")

    

    elif cmd == "INSERT":

        if len(parts) != 9:
            print("Usage: INSERT <table> <Student ID> <First name> <Last name> <age> <semester> <WAM> <Grade>")
            continue

        try:
            table = parts[1]
            key = int(parts[2])

            first_name = parts[3]
            last_name = parts[4]
            WAM = float(parts[7])
            semester = int(parts[6])
            age = int(parts[5])

        except ValueError:
            print("Invalid input: ID/age/semester must be int and WAM must be float")
            continue       
        grade = parts[-1]

        if grade not in allowed_grades:
            print(f"Error: Grade must be one of {allowed_grades}")
            continue
        db.insert(
                table,
                key,
                {
                    "First Name": first_name,
                    "Last Name": last_name,
                    "age": age,
                    "semester": semester,
                    "WAM": WAM,
                    "Grade": grade
                }
            )
        


    elif cmd == "UPDATE":

        if len(parts)!= 9:
            print("Usage: UPDATE <table> <Student ID> <First Name> <Last Name> <age> <semester> <WAM> <Grade>")
            continue

        try:
            table = parts[1]
            key = int(parts[2])

            first_name = parts[3]
            last_name = parts[4]
            WAM = float(parts[7])
            semester = int(parts[6])
            age = int(parts[5])

        except ValueError:
            print("Invalid input: ID/age/semester must be int and WAM must be float")
            continue
        grade = parts[-1]
        if grade not in allowed_grades:
            print(f"Error: Grade must be one of {allowed_grades}")
            continue

        db.update(
            table,
            key,
            {
                "First Name": first_name,
                "Last Name": last_name,
                "age": age,
                "semester": semester,
                "WAM": WAM,
                "Grade": grade
            }
        )

  
    
    elif cmd == "SHOW" and len(parts) >= 2 and parts[1].upper() == "TABLE":

        if len(parts) < 3:
            print("Usage: SHOW TABLE <table_name>")
            continue

        table = parts[2]
        db.show_table(table)
        
    elif cmd == "SHOW":
        if len(parts) >= 2 and parts[1].upper() == "TABLES":
            db.show_tables()
        else:
            print("Usage: SHOW TABLES")

    elif cmd == "DELETE":

        if len(parts) < 3:
            print("Usage: DELETE <table> <key>")
            continue

        try:
            table = parts[1]
            key = int(parts[2])

            db.delete(table, key)

        except ValueError:
            print("Key must be an integer")

    elif cmd == "SELECT":

        if len(parts) < 3:
            print("Usage: SELECT <table> <key>")
            continue

        try:
            table = parts[1]
            key = int(parts[2])

            result = db.select(table, key)
            if result is None:
                print("Record not found")
            else:
                print(result)

        except ValueError:
            print("Key must be an integer")

    elif cmd == "HELP":
        show_help()

    elif cmd == "EXIT":
        print("Shutting down database...")
        break

    else:
        print("Unknown command. Type HELP for usage.")