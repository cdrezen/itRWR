import multixrank as mxk
import pandas as pd
import subprocess
import glob

def cluster_rwr_max_size(path, config_file, out_folder, seeds_file, id, nb_iterations):
    print(id)
    # copy seeds file in output directory
    subprocess.call(["cp", seeds_file, out_folder])
    # write config file in output directory
    file = open(config_file,'r')
    file2 = open(out_folder + '/config.yml', 'w')
    compt = 0
    for k in file :
        print(k)
        if (compt == 0) :
            file2.write('seed: ' + out_folder + f'/seeds_{id}.txt' + '\n')
            compt += 1
        else : 
            file2.write(k)
    file.close()
    file2.close()
    added_nodes = set()

    for i in range(nb_iterations):
        # random walk on the actual set of seed
        multixrank_obj = mxk.Multixrank(config = out_folder + '/config.yml', wdir = path)
        ranking = multixrank_obj.random_walk_rank()
        multixrank_obj.write_ranking(ranking, path = out_folder)
        # open seeds file and put seeds in a set
        file_seeds = open(out_folder + '/' + seeds_file, 'r')
        seeds = set()
        for k in file_seeds :
            temp = k.rstrip('\n')
            seeds.add(temp)
        file_seeds.close()
        
        nodes_data = list()
        nodes = list()
        nodes_name = glob.glob(out_folder + '/multiplex*')

        # open ranking results of RW 
        temp = pd.read_csv(nodes_name[0], sep = '\t')
        temp['node'] = temp['node'].astype(str)
        name = temp['multiplex'][0]
        nodes_data.append(temp)
        nodes.append(name)
        
        for node in temp['node']:
            if node not in seeds:
                seeds.add(node)
                added_nodes.add(node)
                with open(out_folder + '/' + seeds_file, 'w') as seeds_f:
                    for k in seeds :
                        seeds_f.write(k + '\n')
                break