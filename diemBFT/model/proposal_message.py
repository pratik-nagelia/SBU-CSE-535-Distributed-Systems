class ProposalMessage:
    def __init__(self, block, last_round_tc, high_commit_qc):
        self.block = block
        self.last_round_tc = last_round_tc
        self.high_commit_qc = high_commit_qc
        # self.signature = signature
        # self.sender = senders