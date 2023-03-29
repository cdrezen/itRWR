#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itRWR import community_identification
import os

path = os.path.dirname(os.path.realpath(__file__))
path = path + '/'
os.chdir(path)

list_disease = "orpha_codes_toy_ex.txt"
community_identification(path, list_disease, 10)
