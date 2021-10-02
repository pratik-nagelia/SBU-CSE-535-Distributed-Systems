package diem.model;

public class TimeoutMessage {
    TimeoutInfo timeoutInfo;
    TimeoutCertificate lastRoundTC;
    QuorumCertificate highCommitQC;
}
