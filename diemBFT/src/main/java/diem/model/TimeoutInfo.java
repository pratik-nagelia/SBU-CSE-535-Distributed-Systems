package diem.model;

import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
public class TimeoutInfo {

  public int round;
  public QuorumCertificate highQC;
  public int sender;
  public Signature signature;

  public TimeoutInfo(int round, QuorumCertificate highestQc) {
  }
}
