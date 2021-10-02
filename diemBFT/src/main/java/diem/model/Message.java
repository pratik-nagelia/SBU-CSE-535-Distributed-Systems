package diem.model;

public class Message {
    public TimeoutInfo tmoInfo;
    public QuorumCertificate highCommitQC;
    public TimeoutCertificate lastRoundTC;
}
