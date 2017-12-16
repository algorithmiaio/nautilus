#!/usr/bin/env python3
# Author: A. Besir Kurtulmus

# Comparing sentiment analysis algorithms unit-test
# Dataset from: http://ai.stanford.edu/~amaas/data/sentiment/

# To run this test, run the following in the project root directory:
# python -m pytest tests/test_sentiment_algorithmia.py --algorithmia_api_key=simXXXXXXXXXX
from algo import AlgorithmiaAlgorithm
from glue import AlgorithmiaNlpSentimentAnalysis, AlgorithmiaNlpSocialSentimentAnalysis, \
    AlgorithmiaMtmanSentimentAnalysis

def test_define_algorithmia_algorithms1(algorithmia_api_key):
    algo1_name = "nlp/SentimentAnalysis/1.0.4"
    algo1_type = "classification"
    algo1_glue = AlgorithmiaNlpSentimentAnalysis()
    algo1_input = "I like trains."
    algo1_expected_output = 0.3612
    sentiment_algo1 = AlgorithmiaAlgorithm(api_key=algorithmia_api_key,
        algo_name=algo1_name, algo_type=algo1_type, glue=algo1_glue)
    sentiment_algo1.call(algo1_input)

    assert sentiment_algo1.result["compound"] == algo1_expected_output

def test_define_algorithmia_algorithms2(algorithmia_api_key):
    algo1_name = "nlp/SocialSentimentAnalysis/0.1.4"
    algo1_type = "classification"
    algo1_glue = AlgorithmiaNlpSocialSentimentAnalysis()
    algo1_input = "I like trains."
    algo1_expected_output = {}
    algo1_expected_output["positive"] = 0.714
    algo1_expected_output["neutral"] = 0.286
    algo1_expected_output["negative"] = 0.0
    algo1_expected_output["compound"] = 0.3612
    sentiment_algo1 = AlgorithmiaAlgorithm(api_key=algorithmia_api_key,
        algo_name=algo1_name, algo_type=algo1_type, glue=algo1_glue)
    sentiment_algo1.call(algo1_input)

    assert sentiment_algo1.result["positive"] == algo1_expected_output["positive"]
    assert sentiment_algo1.result["neutral"] == algo1_expected_output["neutral"]
    assert sentiment_algo1.result["negative"] == algo1_expected_output["negative"]
    assert sentiment_algo1.result["compound"] == algo1_expected_output["compound"]

def test_define_algorithmia_algorithms2(algorithmia_api_key):
    algo1_name = "mtman/SentimentAnalysis/0.1.1"
    algo1_type = "classification"
    algo1_glue = AlgorithmiaMtmanSentimentAnalysis()
    algo1_input = "I like trains."
    algo1_expected_output = 0.0
    sentiment_algo1 = AlgorithmiaAlgorithm(api_key=algorithmia_api_key,
        algo_name=algo1_name, algo_type=algo1_type, glue=algo1_glue)
    sentiment_algo1.call(algo1_input)

    assert sentiment_algo1.result["compound"] == algo1_expected_output
