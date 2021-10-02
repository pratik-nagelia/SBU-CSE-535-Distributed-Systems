package diem.model;

import java.util.List;

public class TimeoutCertificate {
    public int round;
    public List<Integer> tmoHighQCRounds;
    public List<Signature> tmoSignatures;
}
