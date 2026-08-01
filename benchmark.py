import random
import time
from Database import Database
from lldb import LinkedListDatabase
import matplotlib.pyplot as plt

results = {
    "sizes": [],
    "insert_avl": [],
    "insert_linked": [],
    "search_avl": [],
    "search_linked": [],
    "cache_avl": [],
    "cache_linked": []
}
def generate_records(size):

    records = []

    for i in range(size):
        records.append(
            (
                i,
                {
                    "name": f"Student{i}",
                    "age": random.randint(18, 30),
                    "WAM": round(random.uniform(50, 100), 2)
                }
            )
        )

    return records

def timer(function):

    start = time.perf_counter()

    function()

    end = time.perf_counter()

    return end - start

def run_benchmark(size):

    print(f"\n========== {size} RECORDS ==========")

    records = generate_records(size)

    # Create databases
    avl_db = Database()
    linked_db = LinkedListDatabase()

    avl_db.create_table("students")
    linked_db.create_table("students")


    # ---------------- INSERT ----------------

    def avl_insert():
        for key, value in records:
            avl_db.insert("students", key, value)


    def linked_insert():
        for key, value in records:
            linked_db.insert("students", key, value)


    avl_insert_time = timer(avl_insert)
    linked_insert_time = timer(linked_insert)


    print("\nINSERT")
    print(f"AVL + LRU: {avl_insert_time:.6f}s")
    print(f"Linked:    {linked_insert_time:.6f}s")


    # ---------------- SEARCH ----------------

    search_keys = random.sample(range(size), min(size, 1000))


    def avl_search():
        for key in search_keys:
            avl_db.select("students", key)


    def linked_search():
        for key in search_keys:
            linked_db.select("students", key)


    avl_search_time = timer(avl_search)
    linked_search_time = timer(linked_search)


    print("\nSEARCH")
    print(f"AVL + LRU: {avl_search_time:.6f}s")
    print(f"Linked:    {linked_search_time:.6f}s")


    # ---------------- REPEATED SEARCH ----------------
    # Shows LRU cache advantage

    def avl_cached_search():

        for _ in range(100000):
            avl_db.select("students", size // 2)


    def linked_repeated_search():

        for _ in range(100000):
            linked_db.select("students", size // 2)


    avl_cache_time = timer(avl_cached_search)
    linked_cache_time = timer(linked_repeated_search)


    print("\nREPEATED SEARCH")
    print(f"AVL + Cache: {avl_cache_time:.6f}s")
    print(f"Linked:      {linked_cache_time:.6f}s")

    return {
    "size": size,
    "insert_avl": avl_insert_time,
    "insert_linked": linked_insert_time,
    "search_avl": avl_search_time,
    "search_linked": linked_search_time,
    "cache_avl": avl_cache_time,
    "cache_linked": linked_cache_time
}


if __name__ == "__main__": 

    results = []

    for size in [25000, 50000, 100000]:
        result = run_benchmark(size)
        results.append(result)
    print(result)

    sizes = [r["size"] for r in results]

    plt.plot(
        sizes,
        [r["insert_avl"] for r in results],
        marker="o",
        label="AVL + LRU"
    )

    plt.plot(
        sizes,
        [r["insert_linked"] for r in results],
        marker="o",
        label="Linked List"
    )

    plt.xlabel("Number of Records")
    plt.ylabel("Time (seconds)")
    plt.title("Insert Performance")
    plt.legend()
    plt.grid()
    plt.show()
