package diem.model;

import java.util.List;

public class Block {
    public Author author;
    public int round;
    public List<Transaction> payload;
    public QuorumCertificate quorumCertificate;
    public int id;

    public Block(Author author, int round, List<Transaction> payload, QuorumCertificate quorumCertificate, int id) {
        this.author = author;
        this.round = round;
        this.payload = payload;
        this.quorumCertificate = quorumCertificate;
        this.id = id;
    }
}
