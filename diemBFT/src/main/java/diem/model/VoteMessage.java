package diem.model;

import lombok.AllArgsConstructor;

@AllArgsConstructor
public class VoteMessage {

  public VoteInfo voteInfo;
  public LedgerCommitInfo ledgerCommitInfo;
  public QuorumCertificate highCommitQC;
  public int sender;
  public Signature signature;
}
