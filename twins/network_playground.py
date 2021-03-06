from message import Message

class NetworkPlayground(process):
    def setup(partition_arrangement, twins_mapping):
        self.partition_arrangement = partition_arrangement
        self.twins_mapping = twins_mapping


    def run():
        await False


    def send_message(round, leader, message):
        partitions_wrt_round = partitions_arrangement.get(round)
        partition_of_leader = find_partition(leader)
        other_nodes_in_the_same_partition = find_nodes_in_partition(partition_of_leader)
        for node in other_nodes_in_the_same_partition:
            send(message, node)

    def intra_partition_drop(message):
        partition_view = partitions_arrangement[message.round]
        if partition_view.is_intra_partition_drop == True and partition_view.intra_partiton_drop_message_type == message.message_Type and partition_view.intra_partiton_drop_message_from == message.from
            return True
        else return False

    def filter(message):
        if message.round in drop_round:
            return True
        elif intra_partition_drop(message) == True:
            return True
        else:
            return False



def find_nodes_in_partition(partition):
    pass


def receive(msg=("MESSAGE", message), from_=sender):
        destination  = message.destination

        # Dropping message on filter criteria
        if filter(message):
            return
        partition  = partitions_arrangement[message.round]
        other_nodes_in_the_same_partition = find_nodes_in_partition(partition)
        if destination in other_nodes_in_the_same_partition:
                send((message.message_type, message.payload), to=destination)
        else:
            print("Message Dropped")
        # Sending the message to its twin node as well
        if twinMapping[destination] in other_nodes_in_the_same_partition:
            send((message.message_type, message.payload), to=twinMapping[destination])


