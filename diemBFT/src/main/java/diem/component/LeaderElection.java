package diem.component;

import diem.model.Author;
import diem.model.Block;
import diem.model.QuorumCertificate;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LeaderElection {
    public int validators;
    public int windowSize;
    public int excludeSize;
    Map<Integer, Author> reputationLeaders = new HashMap<>();

    public Author electReputationLeader(QuorumCertificate qc) {
        List<Author> activeValidators = new ArrayList();
        List<Author> lastAuthors = new ArrayList<>();
        QuorumCertificate currentQc = qc;
        for (int i = 0; i < windowSize && lastAuthors.size() < excludeSize; i++) {
            Block currentBlock = Ledger.committedBlock(currentQc.voteInfo.parentId);
            Author blockAuthor = currentBlock.author;
            if (i < windowSize) {
                activeValidators = mergeAuthors(activeValidators, currentQc.signatures.signers());
            }
            if (lastAuthors.size() < excludeSize) {
                lastAuthors = mergeAuthors(lastAuthors, blockAuthor);
            }
            currentQc = currentBlock.quorumCertificate;
        }
        activeValidators.addAll(lastAuthors);
        return activeValidators.get(0);
    }

    public void updateLeaders(QuorumCertificate qc) {
        int extendedRound = qc.voteInfo.parentRound;
        int qcRound = qc.voteInfo.round;
        int currentRound = Pacemaker.currentRound;
        if (extendedRound +1 == qcRound && qcRound+1 == currentRound) {
            reputationLeaders.put(currentRound +1 , electReputationLeader(qc));
        }
    }

    public Author getLeader(Integer round) {
        if (reputationLeaders.containsKey(round)) {
            return reputationLeaders.get(round);
        }
        return roundRobinLeader(validators);
    }

    private Author roundRobinLeader(int validators) {
        // TODO
        return null;
    }

    private List mergeAuthors(List<Author> activeValidators, Author author) {
        // TODO
        return null;
    }
}
