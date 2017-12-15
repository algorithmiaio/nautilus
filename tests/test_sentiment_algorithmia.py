#!/usr/bin/env python3
# Author: A. Besir Kurtulmus

# Comparing sentiment analysis algorithms unit-test
# Dataset from: http://ai.stanford.edu/~amaas/data/sentiment/

# To run this test, run the following in the project root directory:
# python -m pytest tests/test_sentiment_algorithmia.py --algorithmia_api_key=simXXXXXXXXXX
from algos import AlgorithmiaAlgorithm
from glue import AlgorithmiaNlpSentimentAnalysis

def test_define_algorithmia_algorithms(algorithmia_api_key):
    algo1_name = "nlp/SentimentAnalysis/1.0.4"
    algo1_type = "classification"
    algo1_glue = AlgorithmiaNlpSentimentAnalysis()
    algo1_input = "I like trains."
    algo1_expected_output = 0.3612
    sentiment_algo1 = AlgorithmiaAlgorithm(api_key=algorithmia_api_key,
        algo_name=algo1_name, algo_type=algo1_type, glue=algo1_glue)
    sentiment_algo1.call(algo1_input)

    assert sentiment_algo1.result["compound"] == algo1_expected_output
