# -*- generated by 1.0.14 -*-
import da
_config_object = {'channel': 'fifo', 'clock': 'lamport'}
import sys
import json
import logging
author = da.import_da('author')
client = da.import_da('client')

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([])

    def run(self):
        with open(sys.argv[1]) as json_file:
            data = json.load(json_file)
        self.output('CONFIG READ SUCCESSFULLY FROM ', sys.argv[1])
        self.output('Number of Clients Intiated:', data['clients'])
        clients = self.new(client.Client, num=data['clients'])
        validators = self.new(author.Author, num=data['replicas'])
        self.output('Validators Initiated', data['replicas'])
        vNum = 0
        for v in validators:
            self._setup(v, ((validators - {v}), vNum))
            vNum += 1
        self.output('Validators setup done.')
        for c in clients:
            self._setup(c, (validators,))
        self.output('Clients setup done.')
        self._start(validators)
        self._start(clients)
        super()._label('_st_label_271', block=False)
        _st_label_271 = 0
        while (_st_label_271 == 0):
            _st_label_271 += 1
            if False:
                _st_label_271 += 1
            else:
                super()._label('_st_label_271', block=True)
                _st_label_271 -= 1