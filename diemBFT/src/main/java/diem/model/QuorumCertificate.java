package diem.model;


public class QuorumCertificate {
    public VoteInfo voteInfo;
    public LedgerCommitInfo ledgerCommitInfo;
    public Signature signatures;
    public Author author;
    public Signature authorSignature;
}
