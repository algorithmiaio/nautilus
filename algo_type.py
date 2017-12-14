#!/usr/bin/env python3
# Author: A. Besir Kurtulmus

class AlgoTypes(object):
    def __init__(self):
        self.types = ["classification", "regression", "multilabel"]

    def valid_type(self, algo_type):
        if algo_type in self.types:
            return True
        else:
            return False

    def get_types(self):
        return self.types
