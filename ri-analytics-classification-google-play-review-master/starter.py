"""This file starts the microservice"""
#!flask/bin/python
from flask import Flask, json, jsonify, logging, request

from Processor import Processor

with open('./config.json') as config_file:
    CONFIG = json.load(config_file)


app = Flask(__name__)

###########################
# receives a json payload containing a list of app reviews
#   the payload json has to contain at least a list of a single app review that contains the following fields:
#       title   : string
#       body    : string
#       rating  : int
# processes and classifies the raw app reviews
# classifies the processed data
###########################
@app.route("/hitec/classify/domain/google-play-reviews/", methods=["POST"])
def get_classification_result():
    app.logger.debug("1. received request to classify app reviews")

    app_reviews = json.loads(request.data)

    processed_app_reviews = Processor.process(app_reviews)

    return jsonify(processed_app_reviews)


if __name__ == "__main__":
    # app.logger.setLevel(level=logging.DEBUG)
        app.run(debug=False, threaded=False,
                host=CONFIG['HOST'], port=CONFIG['PORT'])
