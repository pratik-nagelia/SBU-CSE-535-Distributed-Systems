class TimeoutMessage:
    def __init__(self, timeout_info, last_round_tc, high_commit_qc):
        self.tmo_info = timeout_info
        self.last_round_tc = last_round_tc
        self.high_commit_qc = high_commit_qc
