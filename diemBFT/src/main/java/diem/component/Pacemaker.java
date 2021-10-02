package diem.component;

import diem.model.QuorumCertificate;
import diem.model.TimeoutCertificate;
import diem.model.TimeoutInfo;

public class Pacemaker {

  public static int currentRound;
  TimeoutCertificate lastRoundTc;
  int pendingTimeouts;
  Safety safety = new Safety();

  public int getRoundTimer(int r) {
    return 1;
  }

  // Revisit
  public int startTimer(int newRound) {
    // Stop Timer
    currentRound = newRound;
    // Start Local Timer
    return 1;
  }

  public void localTimeoutRound() {
    // Save Consensus State
    TimeoutInfo timeoutInfo = safety.makeTimeout(currentRound, BlockTree.highCommitQC, lastRoundTc);
    // broadcast TimeoutMessage
  }

  // Revisit
  public int processRemoteTimeout(TimeoutInfo timeoutInfo) {
    // TimeoutInfo

    if (timeoutInfo.round < currentRound) {
      return 0;
    }

    // Pending Timeout Checks
    return 0;
  }

  public boolean advanceRoundTc(TimeoutCertificate tc) {
    if (tc == null || tc.round < currentRound) {
      return false;
    }
    lastRoundTc = tc;
    startTimer(tc.round + 1);
    return true;
  }

  public boolean advanceRoundQc(QuorumCertificate qc) {
    if (qc.voteInfo.round < currentRound) {
      return false;
    }
    lastRoundTc = null;
    startTimer(qc.voteInfo.round + 1);
    return true;
  }

}
