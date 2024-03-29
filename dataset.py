#!/usr/bin/env python3
# Author: A. Besir Kurtulmus
from Algorithmia import client
import pandas as pd

class Dataset(object):
    '''
    Dataset should be formatted as a pandas DataFrame.
    '''
    def __init__(self, data_world_api_key=None):
        self.data_world_api_key = data_world_api_key
        self.data_set = None
    def get_dataset(self):
        # Override method after inheritance
        return self.data_set

class SentimentDataset(Dataset):
    def __init__(self, data_world_api_key=None):
        super().__init__(data_world_api_key)
        self.positive_sentiment = None
        self.neutral_sentiment = None
        self.negative_sentiment = None
        self.compound_sentiment = None

    def get_positive_sentiment():
        # Override method after inheritance
        return self.positive_sentiment

    def get_neutral_sentiment():
        # Override method after inheritance
        return self.neutral_sentiment

    def get_negative_sentiment():
        # Override method after inheritance
        return self.negative_sentiment

class AppleComputersTwitterSentiment(SentimentDataset):
    def __init__(self, data_world_api_key=None):
        super().__init__(data_world_api_key)
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
        self.lambda_positive_compound_sentiment_confidence = lambda x: x["sentiment:confidence"]
        self.lambda_neutral_compound_sentiment_confidence = lambda x: 0
        self.lambda_negative_compound_sentiment_confidence = lambda x: -1*x["sentiment:confidence"]

    def remove_missing_sentiment(self):
        # Remove any tweet that does not contain information about sentiment
        self.data_set = self.data_set[
            (self.data_set["sentiment"] == "1") |
            (self.data_set["sentiment"] == "3") |
            (self.data_set["sentiment"] == "5")
        ]

    def calculate_compound_sentiment(self):
        self.data_set.loc[(self.data_set["sentiment"] == "5"), "sentiment:compound_confidence"] = \
            self.data_set.apply(self.lambda_positive_compound_sentiment_confidence, axis=1)
        self.data_set.loc[(self.data_set["sentiment"] == "3"), "sentiment:compound_confidence"] = \
            self.data_set.apply(self.lambda_neutral_compound_sentiment_confidence, axis=1)
        self.data_set.loc[(self.data_set["sentiment"] == "1"), "sentiment:compound_confidence"] = \
            self.data_set.apply(self.lambda_negative_compound_sentiment_confidence, axis=1)

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
