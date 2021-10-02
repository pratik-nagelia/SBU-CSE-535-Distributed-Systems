package diem.model;

public class VoteMessage {
    public VoteInfo voteInfo;
    public LedgerCommitInfo ledgerCommitInfo;
    public QuorumCertificate highCommitQC;
    public int sender;
    public Signature signature;
}
