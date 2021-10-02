package diem.model;

import lombok.AllArgsConstructor;

@AllArgsConstructor
public class TimeoutInfo {

  public int round;
  public QuorumCertificate highQC;
  public int sender;
  public Signature signature;
}
