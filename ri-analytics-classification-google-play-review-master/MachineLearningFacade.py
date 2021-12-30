##################
# Author: Christoph Stanik
# Date: 9th June 2017
#
# This class is responsible for:
# 1.0 create a data sample for testing machine learning classifiers
# 2.0 perform machine learning by creating a training model
# 3.0 perform cross validation
# 4.0 compares the results of all classifiers and machine learning features
# 5.0 prints the result of the best performing classifier and machine learning features
#
# Rationale:
# - we want to compare different classifiers
# - we want to compare different combinations of machine learning features
# - we don't want to see the results of all possible combinations and concentrate on the best
##################


class MLFacade:
    @staticmethod
    def get_ml_features(app_review=None, ml_features=None):
        features_single_app_review = []
        if "feature_contains_keywords_bug" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_contains_keywords_bug"])
        if "feature_contains_keywords_feature_request" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_contains_keywords_feature_request"])
        if "feature_tense_past" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_tense_past"])
        if "feature_tense_present" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_tense_present"])
        if "feature_tense_future" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_tense_future"])
        if "feature_rating" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_rating"])
        if "feature_sentiment_score_pos" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_sentiment_score_pos"])
        if "feature_sentiment_score_neg" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_sentiment_score_neg"])
        if "feature_sentiment_score_single" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_sentiment_score_single"])
        if "feature_word_count" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_word_count"])
        if "feature_bow" in ml_features or "all" in ml_features:
            features_single_app_review += app_review["feature_bow"]
        if "feature_bigram" in ml_features or "all" in ml_features:
            features_single_app_review += app_review["feature_bigram"]
        if "feature_keyword_bug" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_keyword_bug"])
        if "feature_keyword_freeze" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_keyword_freeze"])
        if "feature_keyword_crash" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_keyword_crash"])
        if "feature_keyword_glitch" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_keyword_glitch"])
        if "feature_keyword_wish" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_keyword_wish"])
        if "feature_keyword_should" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_keyword_should"])
        if "feature_keyword_add" in ml_features or "all" in ml_features:
            features_single_app_review.append(app_review["feature_keyword_add"])

        return features_single_app_review