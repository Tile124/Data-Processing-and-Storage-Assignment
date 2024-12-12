from inmemorydb import InMemoryDB
print("=================================================================")
print("[START] - InMemoryDB")
# Memory Database object
mm1 = InMemoryDB()

# should return null, because A doesn’t exist in the DB yet
print('> mm1.get("A")')
print(mm1.get("A"))

# should throw an error because a transaction is not in progress
print('> mm1.put("A", 5)')
try:
    mm1.put("A", 5)
except:
    print("Transaction not in process")

# starts a new transaction
print('> mm1.begin_transaction()')
mm1.begin_transaction()

# set’s value of A to 5, but its not committed yet
print('> mm1.put("A", 5)')
mm1.put("A", 5)

# should return null, because updates to A are not committed yet
print('> mm1.get("A")')
print(mm1.get("A"))

# update A’s value to 6 within the transaction
print('> mm1.put("A", 6)')
mm1.put("A", 6)

# commits the open transaction
print('> mm1.commit()')
mm1.commit()

# should return 6, that was the last value of A to be committed
print('> mm1.get("A")')
print(mm1.get("A"))

# throws an error, because there is no open transaction
print('> mm1.commit()')
try:
    mm1.commit()
except:
    print("Transaction not in process")

# throws an error because there is no ongoing transaction
print('> mm1.rollback()')
try:
    mm1.rollback()
except:
    print("Transaction not in process")

# should return null because B does not exist in the database
print('> mm1.get("B")')
print(mm1.get("B"))

# starts a new transaction
print('> mm1.begin_transaction()')
mm1.begin_transaction()

# Set key B’s value to 10 within the transaction
print('> mm1.put("B", 10)')
mm1.put("B", 10)

# Rollback the transaction - revert any changes made to B
print('> mm1.rollback()')
mm1.rollback()

# Should return null because changes to B were rolled back
print('> mm1.get("B")')
print(mm1.get("B"))

print("[END] - InMemoryDB")