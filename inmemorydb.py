class InMemoryDB:
    def __init__(self):
        self._database = {}
        self._prodDatabase = {}
        self.activeTrans = False
        self.throwErrors = False
    
    def put(self, key: str, val: int):
        if self.activeTrans:
            self._prodDatabase.update({key: val})
            pass
        else:
            raise DatabaseError("Transaction not in process")

    def get(self, key: str) -> int:
        got = self._database.get(key)
        return got
    
    def begin_transaction(self):
        if self.activeTrans:
            raise DatabaseError("Transaction already in process")
        else:
            self._prodDatabase = self._database.copy()
            self.activeTrans = True

    def commit(self):
        if self.activeTrans:
            self.activeTrans = False
            self._database = self._prodDatabase.copy()
        else:  
            raise DatabaseError("Transaction not in process")

    def rollback(self):
        if self.activeTrans:
            self.activeTrans = False
        else:  
            raise DatabaseError("Transaction not in process")
        pass

class DatabaseError(Exception):
    pass