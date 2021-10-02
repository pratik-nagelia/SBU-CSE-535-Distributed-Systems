package diem.component;

import diem.model.*;

import java.util.List;

public class BlockTree {
    private List<Block> pendingBlockTree;
    private List<VoteMessage> pendingVotes;
    private QuorumCertificate highQC;
    private QuorumCertificate highCommitQC;


    public void processQC(QuorumCertificate qc) {
        if (qc.ledgerCommitInfo.commitStateId != null) {
            Ledger.commit(qc.voteInfo.parentId);
            // TODO Pending Block tree
//            pendingBlockTree.
            highCommitQC = getMax(qc, highCommitQC);
        }
        highQC = getMax(qc, highQC);
    }

    public void executeAndInsert(Block block) {
        Ledger.speculate(block.quorumCertificate.blockId, block.id, block.payload);;
        pendingBlockTree.add(block);
    }

    public void processVote(VoteMessage vote) {
        processQC(vote.highCommitQC);
        //TODO Implement this code
//        if (pendingVotes == )



    }

    public Block generateBlock(Payload trasaction, int currentRound) {
        return new Block(null, 0, trasaction, highQC, hashCode());
    }


    private QuorumCertificate getMax(QuorumCertificate qc, QuorumCertificate highCommitQC) {
        return null;
    }

}
