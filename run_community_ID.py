from community import *
from create_config_seed_files import *
#from create_config_seed_files import build_seeds_file

path = os.path.dirname(os.path.realpath(__file__))
path = path + '/'
os.chdir(path)
print(path)

# Create dictionary of diseases and associated seeds from ORPHANET
#dico_disease = build_seeds_file("orpha_codes_PA.txt")
dico_seeds_toy_ex = build_seeds_file("orpha_codes_toy_ex.txt")

# Define diseases to analyze
list_diseases_analyzed = [disease for disease in dico_seeds_toy_ex.keys()]

def community_identification(list_diseases: list, nb_iter: int):
    """Function to run community identification for diseases for which 
    identifiers are stored in a list

    Args:
        list_disease (list): list containing identifiers of diseases 
        to analyze
        size (int): the number of iterations we want to set for the 
        recursive random walk with restart algorithm
    """
    for disease in list_diseases:
        config_file = f"config_{disease}.yml"
        out_path = f"results_{nb_iter}_{disease}"
        if not os.path.exists(out_path) :
            os.mkdir(out_path)
        seeds_file = f"seeds_{disease}.txt"
        cluster_rwr_max_size(path=path, config_file=config_file, out_folder=out_path, seeds_file=seeds_file, id=disease, nb_iterations=nb_iter)

community_identification(list_diseases_analyzed, 10)
