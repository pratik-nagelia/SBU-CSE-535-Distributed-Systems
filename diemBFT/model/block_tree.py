from diemBFT.model.block import Block
from quorum_certificate import QC
from ledger_commit_info import LedgerCommitInfo

class BlockTree:
    F = 1
    def __init__(self, pendingBlockTree, pendingVotes, high_qc, high_commit_qc):
        self.pendingBlockTree = pendingBlockTree
        self.pendingVotes = pendingVotes
        self.high_qc = high_qc
        self.high_commit_qc = high_commit_qc

    def process_qc(self, qc):
        if qc is not None and qc.ledger_commit_info.commit_state_id is not None:
            Ledger.commit(qc.vote_info.parent_id)
            # TODO
            self.prune(qc.vote_info.parent_id)
            self.high_commit_qc = self.get_max_round(qc, self.high_commit_qc)
        self.high_qc = self.get_max_round(qc, self.high_qc)

    def executeAndInsert(self, block):
        Ledger.speculate(block.quorum_certificate.block_id, block.block_id, block.payload)
        self.pendingBlockTree.add(block)

    def process_vote(self, vote):
        self.process_qc(vote.high_commit_qc)
        vote_idx = hash(vote.ledger_commit_info)
        self.pending_votes[vote_idx] = self.pending_votes[vote_idx].add(vote.signature)
        if len(self.pending_votes[vote_idx]) == (2 * self.F) + 1:
            signatures_list = list(self.pending_votes[vote_idx])
            new_qc = QC(vote.vote_info, vote.ledger_commit_info, signatures_list, vote.sender, vote.signature)
            return new_qc
        return None

    def generate_block(self, transactions, current_round):
        # TODO
        author = None
        return Block(author, current_round, transactions, self.high_qc, hash(author, current_round, transactions, self.high_qc.vote_info.id, self.high_qc.signatures))

    def get_max_round(self, qc, high_commit_qc):
        pass

    def prune(self, parent_id):
        pass
