package diem.component;

import diem.model.Author;
import diem.model.Block;
import diem.model.LedgerCommitInfo;
import diem.model.Payload;
import diem.model.QuorumCertificate;
import diem.model.Signature;
import diem.model.VoteMessage;
import java.util.List;
import java.util.Map;

public class BlockTree {

  private List<Block> pendingBlockTree;
  private Map<Integer, List<VoteMessage>> pendingVotes;
  private QuorumCertificate highQC;
  static public QuorumCertificate highCommitQC;
  private static final int F = 5;

  public void processQC(QuorumCertificate qc) {
    if (qc.ledgerCommitInfo.commitStateId != null) {
      Ledger.commit(qc.voteInfo.parentId);

      // TODO
      prune(qc.voteInfo.parentId);
      highCommitQC = getMaxRound(qc, highCommitQC);
    }
    highQC = getMaxRound(qc, highQC);
  }

  public void executeAndInsert(Block block) {
    Ledger.speculate(block.quorumCertificate.blockId, block.id, block.payload);
    pendingBlockTree.add(block);
  }

  public QuorumCertificate processVote(VoteMessage vote) {
    processQC(vote.highCommitQC);

    // TODO
    int voteIdx = hash(vote.ledgerCommitInfo);

    if (pendingVotes.containsKey(voteIdx)) {
      List<VoteMessage> voteMessages = pendingVotes.get(voteIdx);
      for (VoteMessage voteMessage : voteMessages) {
        voteMessage.signature = vote.signature;
      }

      if (voteMessages.size() == 2 * F + 1) {

        // TODO Check Creation of QC
        return new QuorumCertificate(vote.voteInfo, vote.ledgerCommitInfo);
      }
    }
    return null;
  }

  public Block generateBlock(Payload payload, int currentRound) {

    //TODO
    Author author = null;

    return new Block(author, currentRound, payload, highQC,
        hash(author, currentRound, payload, highQC.voteInfo.id, highQC.signatures));
  }

  //TODO
  private int hash(Author author, int currentRound, Payload payload, int id, Signature signatures) {
    return 0;
  }


  private static QuorumCertificate getMaxRound(QuorumCertificate qc,
      QuorumCertificate highCommitQC) {
    return null;
  }

  private void prune(int parentId) {

  }

  private int hash(LedgerCommitInfo ledgerCommitInfo) {
    return 0;
  }

}
