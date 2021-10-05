package diem.model;

import lombok.AllArgsConstructor;

@AllArgsConstructor
public class QuorumCertificate {

  public VoteInfo voteInfo;
  public LedgerCommitInfo ledgerCommitInfo;
  public Signature signatures;
  public Author author;
  public Signature authorSignature;
  // TODO Check BlockId not present in the code
  public int blockId;

  public QuorumCertificate(VoteInfo voteInfo, LedgerCommitInfo ledgerCommitInfo) {
  }
}
