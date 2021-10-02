package diem.model;


public class QuorumCertificate {
    VoteInfo voteInfo;
    LedgerCommitInfo ledgerCommitInfo;
    Signature signatures;
    Author author;
    Signature authorSignature;
}
