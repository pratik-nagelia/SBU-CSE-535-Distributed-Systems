class VoteInfo:
    def __init__(self, id, round, parent_id, parent_round, execution_state_id):
        self.id = id
        self.round = round
        self.parent_id = parent_id
        self.parent_round = parent_round
        self.execution_state_id = execution_state_id
