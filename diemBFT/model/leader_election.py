#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''package diem.component;

import diem.model.Author;
import diem.model.Block;
import diem.model.Leader;
import diem.model.QuorumCertificate;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;'''

class LeaderElection:
    F = 1
    def __init__(self,validators, window_size, exclude_size, reputation_leaders):
        self.validators = validators
        self.window_size = window_size
        self.exclude_size = exclude_size
        self.reputation_leaders = reputation_leaders #=> Dict
        
    @staticmethod
    def elect_reputation_leader(self, quorum_certificate):
        active_validators = []
        last_authors = []
        current_qc = quorum_certificate
        
        for(i in range(0,window_size)):
            if(len(last_authors)>=exclude_size):
                break
            current_block = Ledger.committed_block(curren_qc.vote_info.parent_id)
            block_author = current_block.author
            if(i<window_size):
                #TODO
                active_validators = self.merge_authors(active_validators, curren_qc.signatures.signers())
            if(len(last_authors)<exclude_size):
                last_authors = self.merge_authors(last_authors, block_author)
            current_qc = current_block.quorum_certificate
            
            #TODO
            active_validators.extend(last_authors)
            return active_validators[0]
    
    @staticmethod
    def update_leaders(self, quorum_certificate):
        extended_round = quorum_certificate.vote_info.parent_round
        qc_round = quorum_certificate.vote_info.round
        current_round = Pacemaker.current_round
        
        if(extended_round+1==qc_round and qc_round+1==current_round):
            #TODO
            key = current_round+1
            reputation_leaders[key] = elect_reputation_leader(quorum_certificate)
    
    @staticmethod
    def get_leader(self, current_round):
        if(current_round in reputation_leaders):
            return reputation_leaders[current_round]
        return round_robin_leader(validators)
    
    @staticmethod
    def round_robin_leader(self, validators):
        #TODO
        return null

    @staticmethod
    def merge_authors(self, active_validators, author):
        #TODO
        return null

