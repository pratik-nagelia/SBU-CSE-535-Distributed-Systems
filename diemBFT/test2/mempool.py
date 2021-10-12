class MemPool:
    def __init__(self):
        self.q = []

    def addTransaction(self, txn):
        self.q.append(txn)

    def getTransaction(self):
        if len(self.q) > 0:
            return self.q.pop(0)
        return None