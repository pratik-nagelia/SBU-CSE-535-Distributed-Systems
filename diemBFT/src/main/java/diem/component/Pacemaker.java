package diem.component;
import diem.model.*;

public class Pacemaker {
    public static int currentRound;

    public static void advanceRound(int round) {

    }
    public static void advanceRound(TimeoutCertificate tc) {

    }

    public static void advanceRoundTc(TimeoutCertificate lastRoundTC) {
    }

    public static TimeoutCertificate processRemoteTimeout(Message msg) {

        return new TimeoutCertificate();
    }
}
