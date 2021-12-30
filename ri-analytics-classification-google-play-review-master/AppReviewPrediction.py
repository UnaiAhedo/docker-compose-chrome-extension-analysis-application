#########################
# Author: Christoph Stanik Date: 6th August 2017
#
#       Purpose of this script:
# This script classifies reviews by means of binary classification in feature requests, bug reports and others. This script uses already trained models.
#
# Outcome:  a list of app reviews for each of the three classes: feature request, bug report, and others
#########################

import numpy as np

from FileHandler import PickleHandler
from MachineLearningFacade import MLFacade

ml_model_binary_feature_request = None
ml_model_binary_bug_report = None


class Predictor:
    def __init__(self):
        self.ml_features = ["feature_contains_keywords_bug", "feature_contains_keywords_feature_request",
                            "feature_tense_past", "feature_tense_present", "feature_tense_future", "feature_rating",
                            "feature_sentiment_score_pos", "feature_sentiment_score_neg",
                            "feature_sentiment_score_single", "feature_word_count", "feature_bow", "feature_bigram",
                            "feature_keyword_bug", "feature_keyword_freeze", "feature_keyword_crash",
                            "feature_keyword_glitch", "feature_keyword_wish", "feature_keyword_should",
                            "feature_keyword_add"]
        self.ml_model_binary_bug_report = PickleHandler.load_ml_model(
            name="ml_model_bug_report")
        self.ml_model_binary_feature_request = PickleHandler.load_ml_model(
            name="ml_model_feature_request")

    def classify_review(self, app_review):
        features = MLFacade.get_ml_features(
            app_review=app_review, ml_features=self.ml_features)
        is_feature_request = \
            Predictor.predict(app_review=app_review, features=features, ml_model=self.ml_model_binary_feature_request)[
                0] == 0
        is_bug_report = \
            Predictor.predict(app_review=app_review, features=features, ml_model=self.ml_model_binary_bug_report)[
                0] == 0

        app_review["cluster_is_feature_request"] = bool(is_feature_request)
        app_review["cluster_is_bug_report"] = bool(is_bug_report)
        app_review["cluster_is_other"] = bool(
            not is_feature_request and not is_bug_report)

        return app_review

    @staticmethod
    def predict(app_review=None, features=None, ml_model=None):
        if app_review is None or features is None or ml_model is None:
            print("illegal method call")
            return
        return ml_model.predict(np.array([features]))
