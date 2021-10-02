package diem.model;

import java.util.List;

public class TimeoutCertificate {
    int round;
    List<Integer> tmoHighQCRounds;
    List<Signature> tmoSignatures;
}
