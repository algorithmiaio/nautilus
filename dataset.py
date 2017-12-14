#!/usr/bin/env python3
# Author: A. Besir Kurtulmus
from Algorithmia import client

class Dataset(object):
    def __init__(self, api_key):
        self.client = client(api_key)

    def read_dataset(self, abs_dataset_path):
        # Override for loading dataset file into a dataframe
        continue
