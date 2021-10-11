# import sys
# import time
# from safety import Safety
# import constants
# from tc import TC
#
# class Pacemaker:
#     def setup(self, current_round:int, last_round_tc:TC, pending_timeout:dict, validators_count:int):
#         self.current_round = current_round
#         self.last_round_tc = last_round_tc
#         self.round_start_time = None
#         self.round_end_time = None
#         self.pending_timeout = dict()
#         self.validators = validators
#
#     def get_round_time(r):
#         return 4*constants.DELTA
#
#     def stop_time(current_round):
#         self.round_end_time = time.time()
#
#     def start_time(new_round):
#         stop_timer(current_round)
#         current_round = new_round
#         self.round_start_time = time.time()
#         self.round_end_time = time.time() + get_round_time(current_round)
#
#     def local_timeout_rount():
#         timeout_info = Safety.make_timeout(current_round, BlockTree.high_qc, last_round_tc)
#         timeoutmsg = new(timeoutmsg, timeout_info, last_round_tc, BlockTree.high_commit_qc)
#         broadcast(timeoutmsg)
#
#     def broadcast(timeoutmsg):
#         for validator in validators:
#             send((timeoutmsg,), to=validator)
#
#     def process_remote_timeout(timeout_message):
#         timeout_info = timeout_message.timeout_info
#
#         if timeout_info.round < self.current_round:
#             return None
#
#         if timeout_info.sender not in pending_timeout[timeout_info.round]['senders']:
#             pending_timeout[timeout_info.round]['timeout_info'].append(timeout_info)
#             pending_timeout[timeout_info.round]['senders'].append(timeout_info.sender)
#
#         if len(pending_timeout[timeout_info.round]['senders']) == len(validators)+1:
#             stop_time(current_round)
#             local_timeout_round()
#
#         if len(pending_timeout[timeout_info.round]['senders']) == 2*len(validators)+1 :
#             timeout_high_qc_rounds = [timeout_info.round for timeout_info in pending_timeout[timeout_info.round]]
#             signatures = [timeout_info.signature for timeout_info in pending_timeout[timeout_info.round]]
#             return new(TC, round=timeout_info.round, timeout_high_qc_rounds = timeout_high_qc_rounds, timeout_signatures = signatures)
#
#         return None
#
#     def advance_round_tc(tc):
#         if tc==None or tc.round < self.current_round:
#             return False
#
#         self.last_round_tc = tc
#         start_time(tc.round+1)
#         return True
#
#     def timeout_high_qc_rounds(qc):
#         if qc.vote_info.round < self.current_round:
#             return False
#
#         self.last_round_tc = None
#         start_time(qc.vote_info.round+1)
#         return True

class Pacemaker:
    def __init__(self):
        self.currentRound = 0

    def advanceRound(self):
        self.currentRound += 1

    def getCurrentRound(self):
        return self.currentRound

    def setCurrentRound(self, round):
        self.currentRound = round
