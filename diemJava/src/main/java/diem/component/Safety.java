package diem.component;

import diem.model.Block;
import diem.model.LedgerCommitInfo;
import diem.model.QuorumCertificate;
import diem.model.Signature;
import diem.model.TimeoutCertificate;
import diem.model.TimeoutInfo;
import diem.model.VoteInfo;
import diem.model.VoteMessage;
import java.util.Collections;

public class Safety {

  //private String privateKey;
  //private String publicKeys;
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

  //TODO
  private int commitStateIdCandidate(int blockRound, QuorumCertificate qc) {
    if (consecutive(blockRound, qc.voteInfo.round)) {
      return Ledger.pendingState(qc.blockId);
    }
    return -1;
  }

  public VoteMessage makeVote(Block block, TimeoutCertificate lastTc) {
    int qcRound = block.quorumCertificate.voteInfo.round;

    if (validSignature(block, lastTc) && safeToVote(block.round, qcRound, lastTc)) {
      updateHighestQcRound(qcRound);
      increaseHighestVoteRound(block.round);

      VoteInfo voteInfo = new VoteInfo(block.id, block.round, block.quorumCertificate.voteInfo.id,
          qcRound,
          Ledger.pendingState(block.id));

      // Need to Revisit
      LedgerCommitInfo ledgerCommitInfo = new LedgerCommitInfo(
          commitStateIdCandidate(block.round, block.quorumCertificate), hash(voteInfo));

      return new VoteMessage(voteInfo, ledgerCommitInfo, BlockTree.highCommitQC);
    }
    return null;
  }

  private String hash(VoteInfo voteInfo) {
    return null;
  }

  //TODO
  private boolean validSignature(Block b, TimeoutCertificate lastTc) {
    return true;
  }

  public TimeoutInfo makeTimeout(int round, QuorumCertificate highestQc,
      TimeoutCertificate lastTc) {
    int qcRound = highestQc.voteInfo.round;

    if (validSignature(highestQc, lastTc) && safeToTimeout(round, qcRound, lastTc)) {
      increaseHighestVoteRound(round);
      return new TimeoutInfo(round, highestQc);
    }
    return null;
  }

  //TODO
  private boolean validSignature(QuorumCertificate highQc, TimeoutCertificate lastTc) {
    return true;
  }

}
