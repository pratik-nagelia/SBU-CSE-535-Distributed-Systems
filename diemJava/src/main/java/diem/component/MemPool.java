package diem.component;

import diem.model.Payload;

public class MemPool {

  static Payload transactions;

  public static Payload getTransactions() {
    return transactions;
  }
}
