package diem.model;

public class TimeoutInfo {
    int round;
    QuorumCertificate highQC;
    int sender;
    Signature signature;
}
