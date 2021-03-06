import random
import json
import sys
from partition_view import PartitionView


def generate_liveness_partitions(all_nodes):
    liveness = []
    liveness.append(all_nodes)

    return liveness


def generate_ids(honest_nodes_count, faulty_nodes_count):
    total = honest_nodes_count + faulty_nodes_count
    all_nodes = list(range(1, total + 1))
    faulty_nodes = random.sample(all_nodes, faulty_nodes_count)
    honest_nodes = list(set(all_nodes) - set(faulty_nodes))
    return honest_nodes, faulty_nodes


def generate_twins_ids(faulty_nodes):
    faulty_twins = [(item * -1) for item in faulty_nodes]
    return faulty_twins


def generate_test_scenarios(configs):
    total_nodes = configs["total_nodes"]  # read # of non-faulty nodes from config_file
    faulty_nodes_count = configs["faulty_nodes"]  # read # of compromised nodes
    honest_nodes_count = total_nodes - faulty_nodes_count

    # Generate IDs of honest_nodes, faulty nodes and twins.
    honest_nodes, faulty_nodes = generate_ids(honest_nodes_count, faulty_nodes_count)
    faulty_twins = generate_twins_ids(faulty_nodes)

    # Combine all the nodes present in the system
    all_nodes = []
    all_nodes += honest_nodes + faulty_nodes + faulty_twins

    # Generate partitions for all node Ids
    partition_generator = generate_partitions(all_nodes)

    partitions = []
    for partition in partition_generator:
        partitions.append(partition)

    # Selection of leaders : Only faulty leaders or all nodes
    leaders = faulty_nodes.copy()
    if not configs["only_faulty_leaders"]:
        leaders.extend(honest_nodes)

    # Pruning Partitions to remove redundant test cases.
    # TODO
    # partitions = prune_partition_views(partitions, honest_nodes, faulty_nodes, faulty_twins)

    # Liveness testing: Append a partition of all nodes in one set to ensure quorum is created and a commit happens
    partitions.append(generate_liveness_partitions(all_nodes))

    partition_views = assignLeadersToPartitions(leaders, partitions, configs)

    # Step3 Arrange leader-partition pairs over rounds
    round_arrangements = enumerate_partitions(partition_views, configs)

    tag_intra_partition_drop(round_arrangements, configs)

    fileoutput(honest_nodes, faulty_nodes, faulty_twins, round_arrangements)


# Assign leaders to partition. E.g for P1 partition, {A, P1 }, {B,P1}, {C,P1}, {D,P1}
def assignLeadersToPartitions(leaders, partitions, config):
    limit_views = config["enumeration_limit"]["partition_views"]
    # Limit number of leaders to associate with
    selected_leaders = random.sample(leaders, config["enumeration_limit"]["leaders"])
    partition_views = []
    for partition in partitions[0: limit_views]:
        for leader in selected_leaders:
            view = PartitionView(partition, leader, False, None, None)
            partition_views.append(view)
    return partition_views  # Enumeration Limit


# Tag a partion_view till a particular round and message Type for an intra-partition drop
def tag_intra_partition_drop(round_arrangements, config):
    message_type = config["intra_partition_drop_message_type"]
    id = config["intra_partition_drop_message_from"]

    for round in config["intra_partition_drop_rounds"]:
        round_arrangements[round].is_intra_partition_drop = True
        round_arrangements[round].intra_partiton_drop_message_type = message_type
        round_arrangements[round].intra_partiton_drop_from = id


# If enumeration_type is not randomised, it will generate the same deterministic order since the partitioning algo
# generates the same pattern always.
def enumerate_partitions(partiton_views, config):
    if config['enumeration_type'] == 'RANDOMISED':
        random.seed(config["seed"])
        random.shuffle(partiton_views)
    round_arrangements = {}
    for round_no, partition_view in enumerate(partiton_views, 1):
        round_arrangements[round_no] = partition_view
        if round_no >= config["enumeration_limit"]["total_round_views"]:  # Enumeration Limit
            break
    return round_arrangements


# Pruning partitions based on redundancy in the encoding
def prune_partition_views(partition_views, honest_nodes, faulty_nodes, faulty_twins):
    encoding_map = {}
    partitions = []
    for partition_set in partition_views:
        encoding = ""
        for partition in partition_set:
            for node in partition:
                if node in honest_nodes:
                    encoding += "H"
                elif node in faulty_nodes:
                    encoding += "F"
                elif node in faulty_twins:
                    encoding += "T"
            encoding += "|"
        if encoding not in encoding_map:
            partitions.extend(partition_set)
        encoding_map[encoding] = True
    return partitions


# Generates the set of all partitions
def generate_partitions(nodes):
    if len(nodes) == 1:
        yield [nodes]
        return

    first = nodes[0]
    for smaller in generate_partitions(nodes[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[first] + subset] + smaller[n + 1:]
        # put `first` in its own subset
        yield [[first]] + smaller


def fileoutput(honest_nodes, faulty_nodes, faulty_twins, round_arrangements):
    file = open("test_scenarios.json", "w")
    json.dump(round_arrangements, file, default=lambda x: x.__dict__, indent=4)
    file.close()


def main():
    with open(sys.argv[1]) as config_file:
        configs = json.load(config_file)
    generate_test_scenarios(configs)


if __name__ == '__main__':
    main()