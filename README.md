# MiniDB – AVL Tree + LRU Cache Database

## Overview

MiniDB is a simple command-line database written in Python.
It uses an **AVL Tree** for fast indexing and an **LRU Cache** to speed up repeated lookups.

---

## Features

* Create and manage tables
* Insert, select, update, and delete records
* AVL Tree for balanced O(log n) operations
* LRU cache for faster repeated queries
* CLI-based interface

---

## Project Structure

```
MiniDB/
├── main.py        # CLI interface
├── Database.py    # Core database logic
├── AVL.py         # AVL tree implementation
└── LRU.py         # LRU cache implementation
```

---

## How to Run

```bash
python main.py
```

---

## Commands

### Create Table

```
CREATE TABLE <table_name>
```

### Insert

```
INSERT <table> <id> <first> <last> <age> <semester> <wam> <grade>
```

### Select

```
SELECT <table> <id>
```

### Update

```
UPDATE <table> <id> <first> <last> <age> <semester> <wam> <grade>
```

### Delete

```
DELETE <table> <id>
```

### Show Tables

```
SHOW TABLES
```

### Show Table

```
SHOW TABLE <table_name>
```

### Help

```
HELP
```

### Exit

```
EXIT
```

---

## How It Works

* Each table is stored as an **AVL Tree** for fast sorted access
* Records are cached using an **LRU cache** for quick repeated lookups
* Cache hits avoid searching the tree

---

## Key Ideas

* AVL Trees keep data balanced → fast search/insert/delete
* LRU cache improves repeated query performance
* Hashmap + doubly linked list used for O(1) cache operations

---

## Example

```
CREATE TABLE students
INSERT students 1 Alice Smith 20 1 75.5 HD
SELECT students 1
```

---

## Summary

MiniDB is a lightweight database engine demonstrating:

* AVL trees
* caching systems
* basic DB operations
* CLI design
