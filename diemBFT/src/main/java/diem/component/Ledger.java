package diem.component;

import diem.model.Block;
import diem.model.Payload;

public class Ledger {

  public static void commit(int parentId) {

  }

  public static int pendingState(int blockId) {
    return 0;
  }

  public static void speculate(int qcBlockId, int blockId, Payload payload) {

  }


  public static Block committedBlock(int parentId) {
    return null;
  }
}
