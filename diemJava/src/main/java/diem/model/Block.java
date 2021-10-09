package diem.model;

public class Block {

  public Author author;
  public int round;
  public Payload payload;
  public QuorumCertificate quorumCertificate;
  public int id;

  public Block(Author author, int round, Payload payload, QuorumCertificate quorumCertificate,
      int id) {
    this.author = author;
    this.round = round;
    this.payload = payload;
    this.quorumCertificate = quorumCertificate;
    this.id = id;
  }
}
