class TimeoutCertificate:
    def __init__(self, round, tmo_high_qc_rounds, tmo_signatures):
        self.round = round
        self.tmo_high_qc_rounds = tmo_high_qc_rounds
        self.tmo_signatures = tmo_signatures
