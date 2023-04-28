#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itRWR import community_identification
import os

path = os.path.dirname(os.path.realpath(__file__))
path = path + '/'
os.chdir(path)

list_disease = "orpha_codes_toy_ex.txt"
num_iteration = 10
community_identification(path, list_disease, num_iteration)
