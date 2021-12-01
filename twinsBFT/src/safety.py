def check_safety(all_nodes):
    file_map = {}
    # Open all ledger files
    for id in all_nodes:
        filename = "validator_" + str(id) + ".ledger"
        fp = open('../ledgers/config' + str(config_id) + "/" + filename, 'r')
        file_map[id] = fp


check_safety([1,2,3,4,-1])