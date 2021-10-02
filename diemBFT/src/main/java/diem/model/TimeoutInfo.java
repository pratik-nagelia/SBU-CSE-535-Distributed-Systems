package diem.model;

import lombok.AllArgsConstructor;

@AllArgsConstructor
public class TimeoutInfo {

    int round;
    QuorumCertificate highQC;
    int sender;
    Signature signature;
}
