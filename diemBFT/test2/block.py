class Block:
    def __init__(self, round, author, payload):
        self.round = round
        self.id = '123'
        self.author = author
        self.payload = payload

    def __str__(self):
        return 'Round: {}, Payload: {}'.format(self.round, self.payload)
