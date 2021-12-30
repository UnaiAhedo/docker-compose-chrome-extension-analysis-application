from AppReviewPrediction import Predictor
from AppReviewProcessor import AppReviewProcessor


class Processor:
    @staticmethod
    def process(app_reviews):
        predictor = Predictor()
        processor = AppReviewProcessor()
        processed_app_reviews = list()

        for app_review in app_reviews:
            print(app_review)
            print('-----------')
            processed_app_review = processor.process(app_review.copy())
            processed_app_review = predictor.classify_review(
                processed_app_review)

            # omitting the NLP features by adding the classificationr esult to the original app review
            app_review["cluster_is_feature_request"] = processed_app_review["cluster_is_feature_request"]
            app_review["cluster_is_bug_report"] = processed_app_review["cluster_is_bug_report"]
            processed_app_reviews.append(app_review)

        return processed_app_reviews
