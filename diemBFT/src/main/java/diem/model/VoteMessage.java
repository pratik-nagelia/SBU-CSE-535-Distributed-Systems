package diem.model;

public class VoteMessage {
    VoteInfo voteInfo;
    LedgerCommitInfo ledgerCommitInfo;
    QuorumCertificate highCommitQC;
    int sender;
    Signature signature;
}
