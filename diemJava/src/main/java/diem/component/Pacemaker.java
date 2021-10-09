package diem.component;

import diem.model.Block;
import diem.model.QuorumCertificate;
import diem.model.TimeoutCertificate;
import diem.model.TimeoutInfo;
import diem.model.TimeoutMessage;

public class Pacemaker {

  public static int currentRound;
  static TimeoutCertificate lastRoundTc;
  int pendingTimeouts;
  Safety safety = new Safety();

  public static void advanceRound(TimeoutCertificate timeoutCertificate) {
  }

  public static void advanceRound(int round) {
  }

  // TODO
  public int getRoundTimer(int r) {
    return 1; // round timer formulae
  }

  // TODO
  public static void startTimer(int newRound) {
    stopTimer(currentRound);
    currentRound = newRound;
    // Start Local Timer
  }

  private static void stopTimer(int currentRound) {
  }

  public void localTimeoutRound() {
    saveConsensusState();
    TimeoutInfo timeoutInfo = safety.makeTimeout(currentRound, BlockTree.highCommitQC, lastRoundTc);
    TimeoutMessage timeoutMessage = new TimeoutMessage(timeoutInfo, lastRoundTc, BlockTree.highCommitQC);

    //API CALL
    //broadcast TimeoutMessage
  }

  private void saveConsensusState() {
  }

  // TODO
  public static TimeoutCertificate processRemoteTimeout(TimeoutMessage message) {
    TimeoutInfo timeoutInfo = message.getTimeoutInfo();

    if (timeoutInfo.round < currentRound) {
      return null;
    }

    // Pending Timeout Checks
    return null;
  }

  public static boolean advanceRoundTc(TimeoutCertificate tc) {
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
