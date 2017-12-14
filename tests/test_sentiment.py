#!/usr/bin/env python3
# Author: A. Besir Kurtulmus

# Comparing sentiment analysis algorithms unit-test
# Dataset from: http://ai.stanford.edu/~amaas/data/sentiment/

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

def test_load_dataset():
    assert(False)

def test_define_algorithms():
    assert(False)

def test_create_glues():
    assert(False)

def test_create_metrics():
    assert(False)

def test_create_competition():
    assert(False)
