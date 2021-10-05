package diem;

import diem.component.BlockTree;
import diem.component.LeaderElection;
import diem.component.MemPool;
import diem.component.Pacemaker;
import diem.component.Safety;
import diem.model.Block;
import diem.model.Leader;
import diem.model.ProposalMessage;
import diem.model.QuorumCertificate;
import diem.model.TimeoutCertificate;
import diem.model.TimeoutMessage;
import diem.model.VoteMessage;

public class Main {

  BlockTree blockTree;
  //LeaderElection leaderElection;
  //Pacemaker pacemaker;
  Safety safety;

  public Main(BlockTree blockTree, Safety safety) {
    this.blockTree = blockTree;
    this.safety = safety;
  }

  public void processCertificateQc(QuorumCertificate qc) {
    blockTree.processQC(qc);
    LeaderElection.updateLeaders(qc);
    Pacemaker.advanceRound(qc.voteInfo.round);
  }

  void processProposalMsg(ProposalMessage P) {
    processCertificateQc(P.block.quorumCertificate);
    processCertificateQc(P.highCommitQC);
    Pacemaker.advanceRoundTc(P.lastRoundTC);
    int currRound = Pacemaker.currentRound;
    Leader leader = LeaderElection.getLeader(currRound);
    if (P.block.round != currRound || P.sender != leader || leader != P.block.author) {
      return;
    }
    blockTree.executeAndInsert(P.block);
    VoteMessage vote = safety.makeVote(P.block, P.lastRoundTC);
    if (vote != null) {
      Leader nextRoundLeader = LeaderElection.getLeader(currRound + 1);

      // API CALL
      // send(vote, nextRoundLeader);
    }
  }

  void processTimeoutMessage(TimeoutMessage msg) {

    processCertificateQc(msg.getTimeoutInfo().highQC);
    processCertificateQc(msg.getHighCommitQC());
    Pacemaker.advanceRoundTc(msg.getLastRoundTC());
    TimeoutCertificate tc = Pacemaker.processRemoteTimeout(msg);
    if (tc != null) {
      Pacemaker.advanceRound(tc);
      processNewRoundEvent(tc);
    }
  }

  void processVoteMessage(VoteMessage msg) {
    QuorumCertificate qc = blockTree.processVote(msg);
    if (qc != null) {
      processCertificateQc(qc);
      processNewRoundEvent(null);
    }
  }

  void processNewRoundEvent(TimeoutCertificate last_tc) {
    Leader leader = LeaderElection.getLeader(Pacemaker.currentRound);

    if (leader != null) {
      Block b = blockTree.generateBlock(MemPool.getTransactions(), Pacemaker.currentRound);
      ProposalMessage p = new ProposalMessage(b, last_tc, BlockTree.highCommitQC);

      // API CALL
      // broadcast proposal message

    }

  }
}
