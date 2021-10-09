package diem.model;

import lombok.AllArgsConstructor;
import lombok.Data;

@AllArgsConstructor
@Data
public class TimeoutMessage {
    TimeoutInfo timeoutInfo;
    TimeoutCertificate lastRoundTC;
    QuorumCertificate highCommitQC;
}
