#!/usr/bin/env python3
# Author: A. Besir Kurtulmus

# Comparing sentiment analysis algorithms unit-test
# Dataset from: http://ai.stanford.edu/~amaas/data/sentiment/

# To run this test, run the following in the project root directory:
# python -m pytest tests/test_sentiment_dataset.py
from dataset import AppleComputersTwitterSentiment

ds = AppleComputersTwitterSentiment()

def test_dataset_downloaded():
    assert not isinstance(ds, type(None))

def test_verify_positive_sentiment_values():
    # There should only be 423 positive tweets
    assert len(ds.get_positive_sentiment()) == 423

def test_verify_neutral_sentiment_values():
    # There should only be 2162 neutral tweets
    assert len(ds.get_neutral_sentiment()) == 2162

def test_verify_negative_sentiment_values():
    # There should only be 1219 negative tweets
    assert len(ds.get_negative_sentiment()) == 1219

def test_verify_compound_sentiment_values():
    # There should be 3804 compound tweets
    assert len(ds.get_compound_sentiment()) == 3804

def test_verify_compound_scores():
    # Make sure that compound scores are between -1 and 1
    assert min(ds.get_compound_sentiment()["sentiment:compound_confidence"]) >= -1
    assert max(ds.get_compound_sentiment()["sentiment:compound_confidence"]) <= 1
