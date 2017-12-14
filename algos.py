#!/usr/bin/env python3
# Author: A. Besir Kurtulmus
from Algorithmia import client
from glue import *
from algo_type import AlgoTypes

class Algorithm(object):
    '''
    Algorithm is defined as an API endpoint that has a certain function.
    Does not only refer to an Algorithmia algorithm.
    '''
    def __init__(self, api_key, algo_name, algo_type, glue):
        self.types = AlgoTypes()
        self.type = algo_type
        if not self.types.valid_type(self.type):
            raise Exception("Algorithm is not a valid type.")
        self.glue = glue
        self.client = None
        self.algo = None
        self.metadata = None
        self.result = None

    def call(self, input):
        return self.result

class AlgorithmiaAlgorithm(Algorithm):
    '''
    An Algorithmia algorithm.
    '''
    def __init__(self, api_key, algo_name, algo_type, glue):
        super().__init__(api_key, algo_name, algo_type, glue)
        self.client = client(api_key)
        self.algo = self.client.algo(algo_name)

    def call(self, input):
        res = self.algo.pipe(input)
        self.metadata = res.metadata
        self.result = res.result
        return self.result
