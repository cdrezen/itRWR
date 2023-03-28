#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import glob
import re
import os

# Define path for files
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

def build_seeds_file(orpha_seeds: str) -> dict:
    """Function to build seeds file from an input
    file containing ORPHANET disease IDs and
    their corresponding causative genes.
    These causative genes are taken as 
    seeds for the recursive random walk with 
    restart

    Args:
        orpha_seeds (str): file name of
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
            # separate diseases from seeds in the input file
            disease = line.split("\t")[0]
            # split seeds
            seeds_rsplit = line.split("\t")[1].rsplit()
            seeds = [genes.split(",") for genes in seeds_rsplit]
            # initialize key in dico for disease
            dico_seeds[disease] = []
            # writing one seeds file for each set of seeds
            # we take the orpha code of the disease to name the seeds files
            with open(f"seeds_{disease}.txt", 'w') as fo:
                for list_genes in seeds:
                    for genes in list_genes:
                        # add set of seeds in dico
                        dico_seeds[disease].append(genes)
                        # write seeds in the output file
                        fo.write(genes + "\n")
        return dico_seeds

dico_diseases_seeds = build_seeds_file("orpha_codes_PA.txt")

# Define filenames for the layers of the multiplex
layer1 = 'PPI.tsv'
layer2 = 'Pathways.tsv'
layer3 = 'Coexpression.tsv'
layer4 = 'Complexes.tsv'
layer5 = 'Diseases_involvement.tsv'
size = len(glob.glob(path + '/multiplex/*'))

def build_config_files(dico_diseases_seeds: dict) -> None:
    """Function to build configuration files
    for each disease

    Args:
        dico_diseases_seeds (dict): dictionary containing
        disease ORPHANET identifiers and their associated
        seeds

    Return:
        None
    """
    for disease in dico_diseases_seeds:
        file = open(path + f'/config_{disease}.yml', 'w')
        r = 0.7
        delta = 0.5
        tau = [1/5, 1/5, 1/5, 1/5, 1/5]

        file.write(f'seed: seeds_{disease}.txt' + '\n')
        file.write('self_loops: 0' + '\n')
        file.write('r: ' + str(r) + '\n')
        temp = '{},'*size
        part = '[' + temp.rstrip(',') +']'
        file.write('eta: ' + part.format(*[1/size for i in range(size)]) + '\n')
        file.write('multiplex:' + '\n')
        for i in range(size) :
            file.write('    ' + str(i+1) + ':' + '\n' + '        ' + \
                            'layers:' + '\n' + '            ' + \
                                '- multiplex/' + str(i+1) + '/' + layer1 + '\n' + '            ' + \
                                '- multiplex/' + str(i+1) + '/' + layer2 + '\n' + '            ' + \
                                '- multiplex/' + str(i+1) + '/' + layer3 + '\n' + '            ' + \
                                '- multiplex/' + str(i+1) + '/' + layer4 + '\n' + '            ' + \
                                '- multiplex/' + str(i+1) + '/' + layer5 + '\n' + '        ' + \
                                'delta: {}'.format(str(delta)) + '\n' + '        ' + \
                                'graph_type: ' + '[00, 00, 00, 00, 00]' + '\n' + '        ' + \
                                'tau: ' + str(tau) + '\n')
        file.close


build_config_files(dico_diseases_seeds)