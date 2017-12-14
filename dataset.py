#!/usr/bin/env python3
# Author: A. Besir Kurtulmus
from Algorithmia import client
import pandas as pd

class Dataset(object):
    def __init__(self, data_world_api_key=None):
        self.data_world_api_key = data_world_api_key
        self.data_set = None
    def read_dataset(self):
        # Override for loading dataset file into a dataframe
        return self.data_set

class AppleComputersTwitterSentiment(Dataset):
    def __init__(self, data_world_api_key=None):
        self.data_world_api_key = data_world_api_key
        self.data_set = pd.read_csv('https://query.data.world/s/0cUqqvqhsPW532T5HZqFYuWuqWp2mS', encoding='ISO-8859-1')
        self.init_lambda_functions()
        self.remove_missing_sentiment()
        self.calculate_compound_sentiment()
        self.positive_sentiment = self.get_positive_sentiment()
        self.neutral_sentiment = self.get_neutral_sentiment()
        self.negative_sentiment = self.get_negative_sentiment()
        self.compound_sentiment = self.get_compound_sentiment()

    def init_lambda_functions(self):
        self.lambda_compound_sentiment_confidence = lambda x: int(x["sentiment"])*x["sentiment:confidence"]

    def remove_missing_sentiment(self):
        # Remove any tweet that does not contain information about sentiment
        self.data_set = self.data_set[
            (self.data_set["sentiment"] == "1") |
            (self.data_set["sentiment"] == "3") |
            (self.data_set["sentiment"] == "5")
        ]

    def calculate_compound_sentiment(self):
        self.data_set["sentiment:compound_confidence"] = self.data_set.apply(self.lambda_compound_sentiment_confidence, axis=1)

    def get_positive_sentiment(self):
        return self.data_set[(self.data_set["sentiment"] == "5")][["text", "sentiment:confidence"]]

    def get_neutral_sentiment(self):
        return self.data_set[(self.data_set["sentiment"] == "3")][["text", "sentiment:confidence"]]

    def get_negative_sentiment(self):
        return self.data_set[(self.data_set["sentiment"] == "1")][["text", "sentiment:confidence"]]

    def get_compound_sentiment(self):
        return self.data_set[["text", "sentiment:compound_confidence"]]

    def get_dataset(self):
        return self.data_set
