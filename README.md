
# Data Processing and Storage Assignment

An extra credit assignment exploring memory databases with transaction support.





## Prerequisites

- Python 3.6+ installed.

## Installation & running

1. Download `inmemorydb.py` and `tester.py` (optional)

2. Navigate to directory of files (tester.py must be in the same directory of inmemorydb.py)

3. To test, ensure that python is installed and run
```bash
python tester.py
```

4. To use in a project
```python
from inmemorydb import InMemoryDB
# Create a new InMemoryDB object
mm1 = InMemoryDB()
```



## Documentation

`begin_transaction()`: Begins a transaction. Errors, if a transaction is already in process.

`put(key, value)`: Creates new key with value if doesnt exist, otherwise updates existing value. Requires a transaction to be in process.

`get(key)`: Returns int value associated to key, or null (None) if key doesnt exist.

`commit()`: Commits transaction to database.

`rollback()`: Rollsback uncommitted transactions.





## Improvements to assignment
As it currently stands, this is a really well written assignment. 

This assignment could be improved by adding more methods. For example, it would be a nice additional challenge to make a `rollback(int x)` method that is supposed to only rollback `x` amount of database changes.

An effective way to grade would be requiring that the assignment is completed in C++, Java, or Python. This makes writing an autograder script possible (I would recommend providing base files).

One thing that would increase the educational value of this assignment is making it so that transactions needed to be logged and stored, so that any transaction can be reversed.