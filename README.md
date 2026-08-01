# MiniDB – ACID-Compliant AVL Tree Database

## Overview

MiniDB is a lightweight database management system written in Python. It combines an **AVL Tree** indexing engine with an **LRU Cache** to provide efficient record storage and retrieval while supporting persistent storage and core ACID database properties.

The project demonstrates how modern database concepts—including indexing, caching, persistence, transactions, and concurrency control—can be implemented from scratch without relying on external database libraries.

---

## Features

- Create and manage multiple tables
- Insert, select, update, and delete records
- AVL Tree indexing for balanced O(log n) operations
- LRU Cache for O(1) repeated lookups
- Persistent JSON-based storage
- Automatic database loading on startup
- Transaction support
  - Begin transaction
  - Commit
  - Rollback
- Thread-safe operations using re-entrant locks
- Atomic disk writes using temporary files and file replacement
- Command-line interface

---

## ACID Properties

MiniDB implements the core ACID database principles:

### Atomicity

Transactions are executed as a single unit of work.

- Database state is snapshotted before a transaction begins
- Failed commits automatically restore the previous state
- Rollback restores both database contents and cache

### Consistency

- Duplicate primary keys are prevented
- AVL Tree balancing preserves indexing correctness
- Persistent storage always reflects a valid database state

### Isolation

Thread-safe execution is achieved using Python's `threading.RLock()`.

- Only one write transaction may modify the database at a time
- Concurrent operations cannot partially observe in-progress writes

### Durability

Committed transactions are permanently stored using JSON persistence.

To prevent database corruption during crashes:

- Data is first written to a temporary file
- The file is flushed to disk using `fsync()`
- `os.replace()` atomically replaces the previous database file

---

## Storage Engine

MiniDB stores all records inside `database.json`.

When the database starts:

1. The JSON file is loaded.
2. Tables are recreated.
3. Records are reinserted into their AVL Trees.
4. The database is immediately ready for querying.

No manual loading is required.

---

## Indexing

Each table is implemented as an AVL Tree.

Benefits:

- O(log n) insertion
- O(log n) lookup
- O(log n) deletion
- Automatically balanced after updates

---

## Cache

MiniDB includes an LRU (Least Recently Used) cache.

Implementation:

- Hash map
- Doubly linked list

Complexities:

- O(1) lookup
- O(1) insertion
- O(1) eviction

Repeated queries are served directly from cache without traversing the AVL Tree.

---

## Project Structure

```
MiniDB/
├── main.py          # CLI interface
├── Database.py      # Database engine
├── AVL.py           # AVL Tree implementation
├── LRU.py           # LRU Cache
├── storage.py       # Persistent JSON storage
├── benchmark.py     # Performance benchmarking
└── database.json    # Stored database
```

---

## Performance Evaluation

MiniDB was benchmarked against an equivalent database implemented using a linked list.

### Insert Performance

| Records | AVL + Storage | Linked List |
|---------:|--------------:|------------:|
| 1,000 | 2.09 s | 0.013 s |
| 2,500 | 12.96 s | 0.080 s |
| 5,000 | 49.64 s | 0.319 s |

The linked list performs faster inserts because new nodes are added to the front in O(1) time, whereas MiniDB performs AVL tree balancing and persists each write to disk. This benchmark reflects the additional work required to provide indexing, persistence, and transactional guarantees.

---

### Search Performance

| Records | AVL + LRU | Linked List | Improvement |
|---------:|----------:|------------:|------------:|
| 1,000 | 0.00175 s | 0.02541 s | **14.5× faster** |
| 2,500 | 0.00176 s | 0.03311 s | **18.8× faster** |
| 5,000 | 0.00198 s | 0.06492 s | **32.8× faster** |

AVL Tree indexing provides logarithmic search complexity, allowing lookup performance to scale significantly better than a linear linked list.

---

### Repeated Search Performance (Cache)

| Records | AVL + Cache | Linked List | Improvement |
|---------:|------------:|------------:|------------:|
| 1,000 | 0.038 s | 1.342 s | **35× faster** |
| 2,500 | 0.037 s | 3.190 s | **86× faster** |
| 5,000 | 0.037 s | 6.444 s | **174× faster** |

Repeated queries benefit from the LRU cache, which serves cached records in O(1) time without traversing the AVL Tree.

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

## How to Run

```bash
python main.py
```

---

## Technologies

- Python
- AVL Trees
- Doubly Linked Lists
- Hash Maps
- JSON Persistence
- Threading (RLock)
- File Synchronisation (`fsync`)
- Atomic File Replacement (`os.replace`)

---

## Summary

MiniDB demonstrates the implementation of a lightweight database system from first principles, including:

- AVL Tree indexing
- LRU caching
- Persistent storage
- Transaction management
- ACID properties
- Thread-safe concurrency control
- Performance benchmarking