# from ledger import Ledger
#
# class BlockTree:
#     def __init__(self, voteInfo, ledgerCommitInfo, voteMsg, qc, block,pendingBlockTree,pendingVotes,highQC,highCommitQC):
#         self.voteInfo = voteInfo
#         self.ledgerCommitInfo = ledgerCommitInfo
#         self.voteMsg = voteMsg
#         self.qc = qc
#         self.block = block
#         self.pendingBlockTree = pendingBlockTree
#         self.pendingVotes = pendingVotes
#         self.highQC = highQC
#         self.highCommitQC = highCommitQC
#
#     def process_qc(qc):
#         if qc.ledgerCommitInfo.commitStateId is not None:
#             Ledger.commit(qc.vote_info.parent_id)
#             pending_block_tree.prune(qc.vote_info.parent_id)
#             high_commit_qc = maxround {qc, high commit qc}
#         high_qc = maxround{qc, high qc}
#
#     def execute_and_insert(b):
#         Ledger.speculate(b.qc.block id, b.id, b.payload)
#         pending_block_tree.add(b)