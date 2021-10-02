package diem.component;

import diem.model.Block;
import diem.model.QuorumCertificate;
import diem.model.VoteInfo;

import java.util.List;

public class BlockTree {
    private List<Block> pendingBlockTree;
    private List<VoteInfo> pendingVotes;
    private QuorumCertificate highQC;
    private QuorumCertificate highCommitQC;


    public void processQC(QuorumCertificate qc) {
        if (qc.ledgerCommitInfo.commitStateId != null) {
            Ledger.commit(qc.voteInfo.parentId);
        }

    }

}
