# MultiXrank based algorithm for Community Identification using Recursive Random Walk with Restart

.. image:: https://img.shields.io/pypi/pyversions/repRWR.svg
    :target: https://www.python.org
    
.. image:: https://github.com/anthbapt/repRWR/workflows/CI/badge.svg
    :target: https://github.com/anthbapt/repRWR/actions?query=branch%3Amaster+workflow%3ACI
    
 
This repository contains an algorithm allowing to perform a recursive random walk with restart on a multiplex network. This algorithm is based on MultiXrank (https://github.com/anthbapt/multixrank), a Python package allowing to perform random walk with restart on universal multilayer networks.

## Files

* ```community.py``` : Python script containing the function for community identification based on recursive random walk with restart
* ```create_config_seed_files.py``` : Python script to generate the configuration yml files and the files containing the seeds for each disease
* ```run_community_ID.py``` : Main Python script containing the function to automatize the community identification for a list of diseases
* ```orpha_codes_PA.txt``` : File containing Premature Aging disease identifiers and their associated causative genes from ORPHANET (https://www.orpha.net/consor4.01/www/cgi-bin/?lng=ENG)

The ```ToyExample``` folder contains a toy example version of a multiplex network and the associated modified versions of the Python scripts to run community identification for one disease example.

## Usage

After having checked and/or modified the script parameters in accordance to your data, run the following command : 

```python run_community_ID.py```

This will create seeds files, configuration files, and output folders for each disease. The community identified for a disease is contained in the file seeds_ID.txt (where ID is the ORPHANET identifier of the disease) inside the corresponding output folder.

## Example

To test the algorithm on a simple example you can run the version of the script ```run_community_ID.py``` contained in the ```ToyExample``` folder. This will apply community identification for one disease, Hutchinson-Gilford Progeria Syndrom (ORPHANET code 740) on a simple multiplex network, with a maximal number of iterations set to 10 for the recursive random walk with restart algorithm. 

It will generate the following output folder : ```results_10_740```. This folder contains a copy of the configuration file used for the community identification for this disease. It contains also a file ```multiplex_1.tsv``` containing the rankings for each node of the multiplex network after the recursive RWR has been applied. The file ```seeds_740.txt``` contains the nodes of the community identified for the disease. Since we applied 10 iterations of the algorithm, and that the disease has 2 starting seeds, the final community obtained contains 12 nodes. 
