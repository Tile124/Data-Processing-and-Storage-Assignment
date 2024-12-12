class InMemoryDB:
    def __init__(self):
        self._database = {}
    
    def put(self, key: str, val: int):
        self._database.update({key, val})
    
    def get(self, key: str) -> int:
        self._database.get(key)