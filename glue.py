#!/usr/bin/env python3
# Author: A. Besir Kurtulmus
from algo_type import AlgoTypes

class Glue(object):
    '''
    Glue is an I/O adaptor for algorithms. It creates a common standard for
        interacting with algorithms in metrics.

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

    def input(self, user_input):
        # This takes the user input, and casts it into the algo input.
        # override this method
        algo_input = user_input
        return algo_input

    def output(self, algo_output):
        # This takes the algo output, and casts it into the user output.
        # override this method
        user_output = algo_output
        return user_output

class SentimentAnalysisGlue(Glue):
    '''
    Glue object for sentiment analysis.

    Returns sentiment object with positive, neutral, negative and compound
        float values.
    '''
    def __init__(self):
        super().__init__("classification")
        self.sentiment = {}
        self.sentiment["positive"] = None
        self.sentiment["neutral"] = None
        self.sentiment["negative"] = None
        self.sentiment["compound"] = None

class Algorithmia_Nlp_SentimentAnalysis(SentimentAnalysisGlue):
    def __init__(self):
        super().__init__()
        self.input_structure = {}
        self.output_structure = {}
        self.input_structure["document"] = str
        self.output_structure["sentiment"] = float
        self.output_structure["document"] = str

    def input(self, user_input):
        algo_input = {}
        if not isinstance(i, str):
            raise Exception("Input must be a string.")
        algo_input["document"] = i
        return algo_input

    def output(self, algo_output):
        user_output = {}
        self.sentiment["compound"] = algo_output[0]["sentiment"]
        return self.sentiment
