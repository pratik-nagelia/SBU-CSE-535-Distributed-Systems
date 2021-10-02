package diem.model;

import lombok.AllArgsConstructor;

@AllArgsConstructor
public class LedgerCommitInfo {
    public Integer commitStateId;
    public String voteInfoHash;
}
