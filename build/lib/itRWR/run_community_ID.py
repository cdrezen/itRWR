from itRWR.community import *
from itRWR.create_config_seed_files import *
import os


def community_identification(path: str, list_diseases: str, nb_iter: int) -> None:
    """Function to run community identification for diseases for which 
    identifiers are stored in a list

    Args:
        path (str) : path of the working directory
        list_disease (list): list containing identifiers of diseases 
        to analyze
        nb_iter (int): the number of iterations we want to set for the 
        recursive random walk with restart algorithm
    Return:
        None
    """
    dico_diseases_seeds = build_seeds_file(list_diseases)
    build_config_files(path, dico_diseases_seeds)
    # Define diseases to analyze
    list_diseases_analyzed = [disease for disease in dico_diseases_seeds.keys()]
    for disease in list_diseases_analyzed:
        config_file = f"config_{disease}.yml"
        out_path = f"results_{nb_iter}_{disease}"
        if not os.path.exists(out_path) :
            os.mkdir(out_path)
        seeds_file = f"seeds_{disease}.txt"
        cluster_rwr_max_size(path=path, config_file=config_file, out_folder=out_path, seeds_file=seeds_file, id=disease, nb_iterations=nb_iter)

