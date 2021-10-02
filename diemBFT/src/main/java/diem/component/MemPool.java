package diem.component;

import diem.model.Transaction;
import java.util.*;

public class MemPool {
    static List<Transaction> transactions;
    public static List<Transaction> getTransactions() {
        return transactions;
    }
}
