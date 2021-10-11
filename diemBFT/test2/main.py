import pacemaker as pm
import json


class Main:
    def __init__(self, num: int):
        self.pacemaker = pm.Pacemaker()
        self.num = num

    def processProposalMessage(self, proposalMessage):
        self.log('Incoming proposal message - ')
        self.log(str(proposalMessage))
        self.log('Inside process proposal message')
        # print('[MAIN]: local pacemaker round - ' + self.pacemaker.getCurrentRound())
        self.log('incoming pacemaker round - ' + str(proposalMessage.block.round))
        if self.pacemaker.getCurrentRound() <= proposalMessage.block.round:
            self.pacemaker.setCurrentRound(proposalMessage.block.round + 1)
            updatedRound = proposalMessage.block.round + 1
            self.log('Updating local pacemaker round id to ' + str(updatedRound))
            return True
        return False

    def log(self, msg):
        prefix = '[MAIN-' + str(self.num) + '] '
        print(prefix + msg)
