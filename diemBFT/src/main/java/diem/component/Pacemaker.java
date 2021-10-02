package diem.component;

import diem.model.TimeoutCertificate;
import diem.model.TimeoutInfo;

public class Pacemaker {

  int currentRound;
  TimeoutCertificate lastRoundTc;
  int pendingTimeouts;

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

  // Revisit
  public int processRemoteTimeout(TimeoutInfo timeoutInfo) {
    // TimeoutInfo

    if (timeoutInfo.round < currentRound) {
      return 0;
    }
    return 0;
  }

}
