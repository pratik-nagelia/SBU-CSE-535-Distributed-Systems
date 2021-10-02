package diem.model;

public class ProposalMessage {
    Block block;
    TimeoutCertificate lastRoundTC;
    QuorumCertificate highCommitQC;
    Signature signature;
}
