#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''package diem.component;

import diem.model.Block;
import diem.model.LedgerCommitInfo;
import diem.model.QuorumCertificate;
import diem.model.Signature;
import diem.model.TimeoutCertificate;
import diem.model.TimeoutInfo;
import diem.model.VoteInfo;
import diem.model.VoteMessage;
import java.util.Collections;'''

class Safety:
    F = 1
    def __init__(self,private_key, public_key, highest_vote_round, highest_qc_round):
        self.private_key = private_key
        self.public_key = public_key
        self.highest_vote_round = highest_vote_round
        self.highest_qc_round = highest_qc_round
    
    def increase_highest_vote_round(self, voting_round):
        self.highest_vote_round = max(self.highest_vote_round,voting_round)
        
    def update_highest_qc_round(self, qc_round):
        self.highest_qc_round = max(self.highest_qc_round,qc_round)
        
    def consecutive(self, block_round, voting_round):
        if(block_round == voting_round+1):
            return True
        return False
    
    def safe_to_extend(self, block_round, qc_round, timeout_certificate):
        return self.consecutive(block_round, timeout_certificate.round)
    
    def safe_to_vote(self, block_round, qc_round, timeout_certificate):
        if(block_round <= max(self.highest_vote_round, qc_round)):
            return False
        return self.consecutive(block_round, qc_round) or self.safe_to_extend(block_round, qc_round, timeout_certificate)
    
    def safe_to_timeout(self, voting_round, qc_round, timeout_certificate):
        if(qc_round < self.highest_qc_round or voting_round <= max(self.highest_vote_round-1, qc_round)):
            return False
        return self.consecutive(voting_round, qc_round) or self.consecutive(voting_round, timeout_certificate.round)
    
    #TODO
    def commit_state_id_candidate(self, block_round, quorum_certificate):
        if(self.consecutive(block_round,quorum_certificate.vote_info.round)):
            return Ledger.pending_state(quorum_certificate.id) #Confirm quorum_certificate.id
        return -1
    
    def make_vote(self, block, last_timeout_certificate):
        qc_round = block.quorum_certificate.vote_info.round
        if(self.valid_signature(block, last_tc) and self.safe_to_vote(block.round, qc_round, last_timeout_certificate)):
            self.update_highest_qc_round(qc_round)
            self.increase_highest_vote_round(block.round)
            
            #VoteInfo vote_info = VoteInfo(block.id, block.round, block.quorum_certificate.vote_info.id, qc_round, 
            #Ledger.pendingState(block.id)) => Last function needs to be implemented
            
            #Needs revisiting
            #CommitStateIdCandidate candidate = CommitStateIdCandidate(block.round, block.quorum_certificate)
            #LedgerCommitInfo ledger_commit_info = LedgerCommitInfo(candidate, calculate_hash(vote_info))
            
            #BlockTree Check how block_tree's object will be initialized.
            #VoteMsg msg = VoteMsg(vote_info, ledger_commit_info, BlockTree.high_commit_qc) #=> Confirm last parameter
            return msg
        return None
    
    #TODO
    def calculate_hash(self, vote_info):
        return None
    
    #TODO
    def valid_signature(self, block, timeout_certificate):
        return True
    
    def make_timeout(self, voting_round, highest_quorum_certificate, last_timeout_tc):
        qc_round = highest_quorum_certificate.vote_info.round
        if(self.valid_signature(highest_quorum_certificate, last_timeout_tc) and self.safe_to_timeout(voting_round, qc_round, last_timeout_tc)):
            increase_highest_vote_round(voting_round)
            return TimeoutInfo(voting_round, highest_quorum_certificate)
        return None
        


# In[ ]:




