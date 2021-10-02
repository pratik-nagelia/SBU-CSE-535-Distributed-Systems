package diem.model;

import lombok.AllArgsConstructor;

@AllArgsConstructor
public class ProposalMessage {
    public Block block;
    public TimeoutCertificate lastRoundTC;
    public QuorumCertificate highCommitQC;
    public Signature signature;
    public Author sender;


    public ProposalMessage(Block b, TimeoutCertificate last_tc, QuorumCertificate highCommitQC) {
    }
}
