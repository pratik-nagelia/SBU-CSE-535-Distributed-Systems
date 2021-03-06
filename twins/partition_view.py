class PartitionView:
    def __init__(self, partition_set, leader, is_intra_partition_drop, intra_partiton_drop_message_type,
                 intra_partiton_drop_message_from):
        self.partition_set = partition_set
        self.leader = leader
        self.is_intra_partition_drop = is_intra_partition_drop
        self.intra_partiton_drop_message_type = intra_partiton_drop_message_type
        self.intra_partiton_drop_message_from = intra_partiton_drop_message_from


    def __str__(self):
        return "(partition_set= " + str(self.partition_set) + " ,leader= " + str(self.leader) + " ,is_intra_partition_drop= " + str(self.is_intra_partition_drop) + " ,intra_partiton_drop_message_type= " + str(self.intra_partiton_drop_message_type) + " ,intra_partiton_drop_message_from= " + str(self.intra_partiton_drop_message_from) + ")"
