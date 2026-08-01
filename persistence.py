from Database import Database

print("========== FIRST RUN ==========")

# Create database
db = Database()

# Create table
db.create_table("students")

# Insert records
db.insert(
    "students",
    1,
    {
        "name": "John",
        "age": 20,
        "WAM": 85
    }
)

db.insert(
    "students",
    2,
    {
        "name": "Alice",
        "age": 21,
        "WAM": 92
    }
)

db.insert(
    "students",
    3,
    {
        "name": "Bob",
        "age": 19,
        "WAM": 76
    }
)

print("\nDatabase contents:")
db.show_table("students")

print("\nProgram finished.")
print("A JSON file should now exist.")