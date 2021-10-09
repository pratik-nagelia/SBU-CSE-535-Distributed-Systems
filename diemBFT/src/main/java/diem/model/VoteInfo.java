package diem.model;

import lombok.AllArgsConstructor;

@AllArgsConstructor
public class VoteInfo {

    public int id;
    public int round;
    public int parentId;
    public int parentRound;
    public int executionStateId;

}
