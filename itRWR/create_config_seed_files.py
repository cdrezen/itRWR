import glob

def build_seeds_file(orpha_seeds: str) -> dict:
    """Function to build seeds file from an input
    file containing ORPHANET disease IDs and
    their corresponding causative genes.
    These causative genes are taken as 
    seeds for the iterative random walk with 
    restart

    Args:
        orpha_seeds (str): name of
        the file containing ORPHANET codes 
        of diseases and their corresponding
        seeds

    Return :
        dict : a dictionary with ORPHANET codes
        as keys and the list of associated seeds 
        as values
    """
    dico_seeds = {}
    with open(orpha_seeds, 'r') as fi:
        for line in fi:
            values = line.strip().split("\t")
            if len(values) > 1:
                # separate diseases from seeds in the input file
                disease = line.split("\t")[0]
                seeds_rsplit = line.split("\t")[1].rsplit()
                seeds = [genes.split(",") for genes in seeds_rsplit]
                # initialize key in dico for disease
                dico_seeds[disease] = []
                # writing one seeds file for each set of seeds
                # we take the ORPHANET code of the disease to name the seeds files
                with open(f"seeds_{disease}.txt", 'w') as fo:
                    for list_genes in seeds:
                        for genes in list_genes:
                            # add set of seeds in dico
                            dico_seeds[disease].append(genes)
                            # write seeds in the output file
                            fo.write(genes + "\n")
        return dico_seeds


def build_config_files(path: str, dico_diseases_seeds: dict) -> None:
    """Function to build configuration files
    for each disease

    Args:
        path (str) : path of the working directory
        dico_diseases_seeds (dict): dictionary containing
        disease ORPHANET identifiers and their associated
        seeds

    Return:
        None
    """
    layers = glob.glob(path + '/multiplex/1/*')
    size = len(layers)
    layers = sorted([layers[i].split('/multiplex/1/')[1] for i in range(size)])
    for disease in dico_diseases_seeds:
        file = open(path + f'/config_{disease}.yml', 'w')
        r = 0.7
        delta = 0.5
        eta = 1.0
        tau = [1/size for _ in range(size)]

        file.write(f'seed: seeds_{disease}.txt' + '\n')
        file.write('self_loops: 0' + '\n')
        file.write('r: ' + str(r) + '\n')
        temp = '{},'*size
        part = '[' + temp.rstrip(',') +']'
        file.write('eta: ' + '[' + str(eta) + ']' + '\n')
        file.write('multiplex:' + '\n')
        
        file.write('    ' + str(1) + ':' + '\n' + '        ' + \
                        'layers:' + '\n' + '            ')
        for i in range(size) :
            if i < size - 1 :
                file.write('- multiplex/' + str(1) + '/' + layers[i] + '\n' + '            ' )
            else :
                file.write('- multiplex/' + str(1) + '/' + layers[i] + '\n' + '        ')
        file.write('delta: {}'.format(str(delta)) + '\n' + '        ' )
        file.write('graph_type: ' + '[' + ('00, '*size).rstrip(', ') + ']' + '\n' + '        ' )
        file.write('tau: ' + str(tau) + '\n')
        file.close