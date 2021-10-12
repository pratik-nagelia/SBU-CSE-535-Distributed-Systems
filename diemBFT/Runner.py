# -*- generated by 1.0.14 -*-
import da
_config_object = {}
import json
import sys
Node = da.import_da('node')
Client = da.import_da('client')
if (__name__ == '__main__'):
    main()

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([])
    _config_object = {'clock': 'Lamport', 'channel': 'fifo'}

    def run(self):
        with open(sys.argv[1]) as config_file:
            conf = json.load(config_file)
        nodes = self.new(Node, num=conf['nodes'])
        self.output('**[Runner]** Number of Nodes Intiated: ', len(nodes))
        clients = self.new(Client, num=conf['clients'])
        self.output('**[Runner]** Number of Clients Intiated: ', len(clients))
        id = 0
        nodeDict = {}
        for n in nodes:
            nodeDict[id] = n
            id += 1
        id = 0
        for n in nodes:
            self._setup(n, (id, nodes, nodeDict))
            self._start(n)
            id += 1
        self.output('**[Runner]** Setup Complete for Nodes')
        id = 0
        for c in clients:
            self._setup(c, (nodes, id))
            self._start(c)
            id += 1