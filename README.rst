=============================================================================================
itRWR : MultiXrank based algorithm for Community Identification using Iterative Random Walk with Restart
=============================================================================================

.. image:: https://github.com/anthbapt/itRWR/workflows/CI/badge.svg
    :target: https://github.com/anthbapt/itRWR/actions?query=branch%3Amaster+workflow%3ACI
 
This repository presents an algorithm allowing to perform an iterative random walk with restart on a multiplex network (i.e., a network composed of multiple layers of interactions sharing the same nodes but different types of edges). It is based on 
MultiXrank (https://github.com/anthbapt/multixrank), a Python package allowing to perform random walk with restart on universal multilayer networks (i.e., networks composed of any combination of multiplex and monoplex networks and their bipartite relationships).

-----------------
 Installation
-----------------

                                
.. code-block:: bash    

  $ python setup.py install

         
-----------------
 Library Codes
-----------------

* ``community.py`` : Python script containing the function for community identification based on iterative Random Walk with Restart
* ``create_config_seed_files.py`` : Python script to generate the configuration yml files and the files containing the seeds to be used for the Random Walk with Restart. To identify disease-associated communities, for instance, the seeds can be the disease causative gene(s)
* ``run_community_ID.py`` : Main Python script containing the function to automatize community identification for different sets of nodes used as seed(s)


-----------------
Data
-----------------


``ToyExample/multiplex`` : This folder contains a subset toy example of a multiplex biological network composed of five layers (PPI, Pathways, Co-expression, Complexes, Disease involvement). This subset is extracted from complete networks, which are available on the NDEX server: `<https://www.ndexbio.org/index.html#/search?searchType=All&searchString=cecile.beust&searchTermExpansion=false>`_

``data/orpha_codes_PA.txt`` : File containing Premature Aging disease identifiers and their associated causative genes from ORPHANET (`<https://www.orpha.net/consor4.01/www/cgi-bin/?lng=ENG>`_). The associated causative genes are used as seed(s) in our study

-----------------
Usage
-----------------

Make sure that the networks you whish to use are stored in a folder named ``multiplex/1/`` in your current directory.
After having checked and/or modified the script parameters in accordance to your data, set the desired number of iterations and run the following Python code: 

.. code-block:: python

    from itRWR import community_identification 
    import os

    path = os.path.dirname(os.path.realpath(__file__))
    path = path + '/'
    os.chdir(path)

    list_disease = "orpha_codes_PA.txt"
    num_iteration = 10
    community_identification(path, list_disease, num_iteration)


This will create seed files, configuration files, and output folders needed for each community disease. The community identified for a disease is contained in the file seeds_ID.txt (In this example, ID is the ORPHANET identifier of the disease) inside the corresponding output folder.

-----------------
Example
-----------------
To test the algorithm on a simple example you can run the version of the script ``run.py`` contained in the ``ToyExample`` folder. This will apply community identification for one disease, Hutchinson-Gilford Progeria Syndrome (ORPHANET code: 740) on the toy example multiplex network, with a number of iterations set to 10 for the itRWR algorithm. 

It will generate the following output folder ``results_10_740`` containing the following files :
 
* ``config.yml``: a copy of the configuration file for the disease
* ``multiplex_1.tsv``: a file containing the rankings for each node of the multiplex network after the itRWR algorithm has been applied
* ``seeds_740.txt``: a file containing the nodes of the community identified for the disease. Since we applied 10 iterations of the algorithm, and that the disease has 2 starting seeds, the final community obtained contains 12 nodes. 
