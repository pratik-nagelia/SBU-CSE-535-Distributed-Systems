package diem.component;

import diem.model.Block;
import diem.model.QuorumCertificate;
import diem.model.VoteMessage;
import diem.model.*;

import java.util.List;

public class BlockTree {

    private List<Block> pendingBlockTree;
    private List<VoteMessage> pendingVotes;
    private QuorumCertificate highQC;
    static public QuorumCertificate highCommitQC;


    public void processQC(QuorumCertificate qc) {
        if (qc.ledgerCommitInfo.commitStateId != null) {
            Ledger.commit(qc.voteInfo.parentId);
            // TODO Pending Block tree
//            pendingBlockTree.
            highCommitQC = getMax(qc, highCommitQC);
        }
        highQC = getMax(qc, highQC);
    }

    // Revisit
    public void executeAndInsert(Block block) {
        Ledger.speculate(block.quorumCertificate.blockId, block.id, block.payload);
        pendingBlockTree.add(block);
    }

    public QuorumCertificate processVote(VoteMessage vote) {
        processQC(vote.highCommitQC);
        //TODO Implement this code
//        if (pendingVotes == )
        QuorumCertificate qc = null;
        return qc;
    }

    public Block generateBlock(List<Transaction> transaction, int currentRound) {
        return new Block(null, 0, transaction, highQC, hashCode());
    }


    private static QuorumCertificate getMax(QuorumCertificate qc, QuorumCertificate highCommitQC) {
        return null;
    }

}
