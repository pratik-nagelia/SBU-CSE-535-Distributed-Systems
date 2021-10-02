package diem.component;

import diem.model.*;

import java.util.Collections;

public class Safety {

    private String privateKey;
    private String publicKeys;
    private int highestVoteRound;
    private int highestQcRound;

    private void increaseHighestVoteRound(int round) {
        highestVoteRound = Math.max(round, highestVoteRound);
    }

    private void updateHighestQcRound(int qcRound) {
        highestQcRound = Math.max(highestQcRound, qcRound);
    }

    private boolean consecutive(int blockRound, int round) {
        return round + 1 == blockRound;
    }

    // Need to Revisit
    private boolean safeToExtend(int blockRound, int qcRound, TimeoutCertificate tc) {
        return consecutive(blockRound, tc.round) && qcRound >= Collections.max(tc.tmoHighQCRounds);
    }

    private boolean safeToVote(int blockRound, int qcRound, TimeoutCertificate tc) {
        if (blockRound <= Math.max(highestVoteRound, qcRound)) {
            return false;
        }
        return consecutive(blockRound, qcRound) || safeToExtend(blockRound, qcRound, tc);
    }

    private boolean safeToTimeout(int round, int qcRound, TimeoutCertificate tc) {
        if (qcRound < highestQcRound || round <= Math.max(highestVoteRound - 1, qcRound)) {
            return false;
        }
        return consecutive(round, qcRound) || consecutive(round, tc.round);
    }

    // Need to Revisit
    private int commitStateIdCandidate(int blockRound, QuorumCertificate qc) {
        if (consecutive(blockRound, qc.voteInfo.round)) {
            return Ledger.pendingState(0);
        }
        return -1;
    }

    public VoteMessage makeVote(Block b, TimeoutCertificate lastTc) {
        int qcRound = b.quorumCertificate.voteInfo.round;

        // Add Valid Signature
        if (safeToVote(b.round, qcRound, lastTc)) {
            updateHighestQcRound(qcRound);
            increaseHighestVoteRound(b.round);
            VoteInfo voteInfo = new VoteInfo(b.id, b.round, b.quorumCertificate.voteInfo.id, qcRound,
                    Ledger.pendingState(b.id));

            // Need to Revisit
            LedgerCommitInfo ledgerCommitInfo = new LedgerCommitInfo(
                    commitStateIdCandidate(b.round, b.quorumCertificate), String.valueOf(voteInfo.id));
            return new VoteMessage(voteInfo, ledgerCommitInfo, BlockTree.highCommitQC, 0,
                    new Signature());
        }
        return null;
    }

    public TimeoutInfo makeTimeout(int round, QuorumCertificate highestQc,
                                   TimeoutCertificate lastTc) {
        int qcRound = highestQc.voteInfo.round;

        // Add Valid Signature
        if (safeToTimeout(round, qcRound, lastTc)) {
            increaseHighestVoteRound(round);
            return new TimeoutInfo(round, highestQc, 0, new Signature());
        }
        return null;
    }

}
