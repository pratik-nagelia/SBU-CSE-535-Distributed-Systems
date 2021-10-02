package diem.component;

import diem.model.QuorumCertificate;
import diem.model.TimeoutCertificate;
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

}
