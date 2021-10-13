# -*- generated by 1.0.14 -*-
import da
_config_object = {}
Block = da.import_da('block')
Ledger = da.import_da('ledger')
VoteInfo = da.import_da('vote_info')
VoteMsg = da.import_da('vote_message')

class BlockTree():
    F = 1

    def __init__(self, pendingBlockTree, pendingVotes, high_qc, high_commit_qc):
        self.pendingBlockTree = pendingBlockTree
        self.pendingVotes = pendingVotes
        self.high_qc = high_qc
        self.high_commit_qc = high_commit_qc
        self.ledger = None
        self.node_id = None

    def set_ledger(self, ledger):
        self.ledger = ledger

    def set_node_id(self, node_id):
        self.node_id = node_id

    def process_qc(self, qc):
        print('Block-Tree Process QC')
        if ((not (qc is None)) and (not (qc.ledger_commit_info.commit_state_id is None))):
            Ledger.commit(qc.vote_info.parent_id)
            self.prune(qc.vote_info.parent_id)
            self.high_commit_qc = self.get_max_round(qc, self.high_commit_qc)
        self.high_qc = self.get_max_round(qc, self.high_qc)

    def execute_and_insert(self, block):
        print('[Block-Tree-Node-{}'.format(self.node_id), '] Execute and insert')
        block_qc_block_id = None
        if (not (block.qc is None)):
            block_qc_block_id = block.qc.block_id
        self.ledger.speculate(block_qc_block_id, block.block_id, block.payload)
        self.pendingBlockTree.append(block)

    def process_vote(self, vote_msg):
        VoteInfo1 = VoteInfo.VoteInfo(0, 0, 0, 0, None)
        vote_msg = VoteMsg.VoteMsg(VoteInfo1, None, None, None, None)
        vote_info = vote_msg.vote_info
        print('[Block-Tree] Process Vote Message with id [{}]'.format(79))
        if (not (vote_msg.high_commit_qc is None)):
            print('[Block-Tree] high_commit_qc of current vote message is not null. See if a commit can be made')
            self.process_qc(vote.high_commit_qc)
        vote_idx = self.hash_determine_id_of_vote(vote_msg.ledger_commit_info)
        print('[Block-Tree] VOTE_IDX: [{}]'.format(vote_idx))
        'self.pending_votes[vote_idx] = self.pending_votes[vote_idx].add(vote.signature)\n        if len(self.pending_votes[vote_idx]) == (2 * self.F) + 1:\n            signatures_list = list(self.pending_votes[vote_idx])\n            new_qc = QC(vote.vote_info, vote.ledger_commit_info, signatures_list, vote.sender, vote.signature)\n            return new_qc\n        return None'

    def generate_block(self, transactions, current_round):
        author = 0
        vote_info_id = None
        high_qc_signatures = None
        if (not (self.high_qc is None)):
            vote_info_id = self.high_qc.vote_info.id
            high_qc_signatures = self.high_qc.signatures
        return Block.Block(author, current_round, transactions, self.high_qc, self.hash_fun(author, current_round, transactions, vote_info_id, high_qc_signatures))

    def get_max_round(self, qc, high_commit_qc):
        pass

    def prune(self, parent_id):
        pass

    def hash_fun(self, author, current_round, transactions, vote_info_id, high_qc_signatures):
        temp_str = (str(author) + str(current_round))
        for t in transactions:
            temp_str = (temp_str + t)
        if (not (vote_info_id is None)):
            temp_str = (temp_str + str(vote_info_id))
        if (not (high_qc_signatures is None)):
            temp_str = (temp_str + str(high_qc_signatures))
        print('[Block-Tree] temp_str: {}'.format(temp_str), ' hash: {}'.format(hash(temp_str)))
        return hash(temp_str)

    def hash_determine_id_of_vote(self, commit_info):
        return 0
