#!/usr/bin/env python3
# Author: A. Besir Kurtulmus
from algo_type import AlgoTypes

class Glue(object):
    '''
    Glue is an adaptor for algorithm I/O's. It creates a common standard for
        calling algorithms.

    Currently 3 types of glues are supported: classification, regression and
        multilabel.
    '''
    def __init__(self, algo_type):
        self.input_structure = None
        self.output_structure = None
        self.types = AlgoTypes()
        self.type = algo_type
        if not self.types.valid_type(self.type):
            raise Exception("Algorithm is not a valid type.")

    def input(self, algo_input):
        # override this method
        return algo_input

    def output(self, algo_output):
        # override this method
        return algo_output
