import json
import sys
from network_playground import NetworkPlayground


def setup_network_playground():
    # runtime = consensus_runtime()
    playground = new(NetworkPlayground)
    return playground


def run_test_executor(test_scenarios, playground):
    honest_nodes = test_scenarios["honest_nodes"]
    faulty_nodes = test_scenarios["faulty_nodes"]
    twins = test_scenarios["twins"]
    round_arrangements = test_scenarios["round_arrangements"]
    playground.initialize_network_playground(round_arrangements)

    setup_deim(all_nodes, twins, round_arrangements)
    execute_test_scenarios()

    check_safety(round_arrangements.values)
    check_liveness(round_arrangements, nodesDict.values())


def setup_deim(honest_nodes, faulty_nodes, twins, round_arrangements, playground):
    round_leader_mapping = get_round_leader_mapping(round_arrangements)
    # Generate round leader mapping from round_arrangements

    honest_nodes_map = generate_nodes(honest_nodes, round_leader_mapping, playground)
    faulty_nodes_map = generate_nodes(compromised_nodes, round_leader_mapping, playground)
    twins_map = generate_twins(faulty_nodes, round_leader_mapping, playground)
    clients_list = generate_clients(honest_nodes_map, faulty_nodes_map)

def generate_nodes(num_of_nodes: int, round_leader_mapping, playground):
    nodes = new(Node, num_of_nodes)
    for node in nodes:
        nodesDict[id] = []
        nodeDict[id].append(node)
        setup(node, (id, round_leader_mapping, playground))
        id+=1


def generate_twins(faulty_nodes, round_leader_mapping, playground):
    for node in faulty_nodes:
        id = node.id
        twin_node = new(Node, 1)
        nodesDict[id].append(twin_node)
        setup(twin_node, (id, round_leader_mapping, playground))
        twinMapping[id] = twin_node


def execute_test_scenario():
    for node in nodesDict.values():
        start(node)

    for client in clients.values():
        start(client)

def check_safety(rounds):
    for i in range(rounds, 1):
        commit_state_id = []
        for j in nodesDict.values():
            commit_state_id[j] = nodes.Ledger.committed_block (round)
        flag = compare(commit_state_id)
        if flag:
            print("Safety Ensured in this round " + str(i))
        else :
            print("Safety violated in this round " + str(i))


def liveness_test(round_arrangements, nodes):
    n = len(nodes)
    last_n_rounds = round_arrangements.values [0 : -1 * n]
    commit = []
    for round_number in last_n_round:
        for j in nodes:
            commit[j] = nodes.Ledger.committed_trasaction(round_number)
    if any_transaction_committed(commit) :
        print("Liveness is confirmed in the last n round ")
    else :
        print("Liveness violated in last n rounds")


def main():
    with open(sys.argv[1]) as test_scenarios_file:
        test_scenarios = json.load(test_scenarios_file)
    network_playground = setup_network_playground()
    run_test_executor(test_scenarios, network_playground)


if __name__ == '__main__':
    main()