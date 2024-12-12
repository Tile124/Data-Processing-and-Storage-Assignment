from inmemorydb import InMemoryDB

# Memory Database object
mm1 = InMemoryDB()

mm1.put("Ryan", 65)

print(mm1.get("Ryan"))
mm1.put("Ryan", 1)
print(mm1.get("Ryan"))
print(mm1.get("Ry"))