from timeout_message import TimeoutMessage
from block_tree import BlockTree


class Pacemaker:
    def __init__(self, current_round, last_round_tc, pending_timeouts):
        self.current_round = current_round
        self.last_round_tc = last_round_tc
        self.pending_timeouts = pending_timeouts


    def get_round_timer(self, r):
        return round_timer_formula

    def star_timer(self, new_round):
        stop_timer(self.current_round)

    def stop_timer(self, current_round):
        pass

    def local_timeout_round(self):
        save_consensus_state()
        timeout_info = Safety.make_timeout(self.current_round, BlockTree.high_qc, last_round_tc)
        broadcast TimeoutMessage(timeout_info, last_round_tc, BlockTree.high_commit_qc)

    def process_remote_timeout(self, tmo):
        tmo_info = tmo.tmo_info

    def advance_round(self, tc):
        if tc is None or tc.round < self.current_round:
            return False
        last_round_tc = tc
        start_timer(tc.round + 1)
        return True

    def advance_round_qc(self, qc):
        if qc.vote_info.round < self.current_round:
            return False
        last_round_tc = None
        start_timer(qc.vote_info.round + 1)
        return True


