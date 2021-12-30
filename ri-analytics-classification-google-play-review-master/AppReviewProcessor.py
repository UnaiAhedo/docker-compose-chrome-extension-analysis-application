import os
import re
import shlex
import subprocess

import nltk
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import CountVectorizer

from FileHandler import PickleHandler


class AppReviewProcessor:
    def __init__(self):
        # needed for the full feature set
        self.vectorizer_bow = self.get_bow_vectorizer()
        self.vectorizer_bigram = self.get_bigram_vectorizer()

    def process(self, app_review):
        original_review = app_review["title"] + " " + app_review["body"]
        review = original_review.strip().lower()
        review = NLPHelper.remove_stopwords(review)
        review = NLPHelper.lem(review)
        review_tense = NLPHelper.count_tense_occurrences(review)
        review_sentiment = NLPHelper.get_sentiment(original_review)

        processed_app_review = app_review
        if "_id" in processed_app_review:
            processed_app_review["_id"] = str(processed_app_review["_id"])
        processed_app_review["full_review"] = (
            app_review["title"] + " " + app_review["body"]).strip()
        processed_app_review["feature_bigram"] = self.vectorizer_bigram.transform(
            [review]).toarray().tolist()[0]
        processed_app_review["feature_bow"] = self.vectorizer_bow.fit_transform(
            [review]).toarray().tolist()[0]
        processed_app_review["feature_keyword_bug"] = review.count("bug")
        processed_app_review["feature_keyword_freeze"] = review.count("freeze")
        processed_app_review["feature_keyword_crash"] = review.count("crash")
        processed_app_review["feature_keyword_glitch"] = review.count("glitch")
        processed_app_review["feature_keyword_wish"] = review.count("wish")
        processed_app_review["feature_keyword_should"] = review.count("should")
        processed_app_review["feature_keyword_add"] = review.count("add")
        processed_app_review["feature_tense_past"] = review_tense.no_past
        processed_app_review["feature_tense_present"] = review_tense.no_present
        processed_app_review["feature_tense_future"] = review_tense.no_future
        processed_app_review["feature_rating"] = app_review["rating"]
        processed_app_review["feature_sentiment_score_pos"] = NLPHelper.get_sentiment_pos_score(
            review_sentiment)
        processed_app_review["feature_sentiment_score_neg"] = NLPHelper.get_sentiment_neg_score(
            review_sentiment)
        processed_app_review["feature_sentiment_score_single"] = NLPHelper.get_sentiment_single_score(
            review_sentiment)
        processed_app_review["feature_word_count"] = NLPHelper.extract_word_cont(
            original_review)
        processed_app_review["feature_contains_keywords_bug"] = NLPHelper.extract_keyword_freq(
            feature="bug", text=original_review)
        processed_app_review["feature_contains_keywords_feature_request"] = NLPHelper.extract_keyword_freq(
            feature="feature", text=original_review)

        return processed_app_review

    @staticmethod
    def get_bow_vectorizer():
        vocabulary_bow = PickleHandler.load_vocabulary(name="bow")

        return CountVectorizer(vocabulary=vocabulary_bow)

    @staticmethod
    def get_bigram_vectorizer():
        vocabulary_bigram = PickleHandler.load_vocabulary(name="bigram")
        vectorizer_bigram = CountVectorizer(ngram_range=(
            2, 2), token_pattern=r'\b\w+\b', min_df=10)
        vectorizer_bigram.fit_transform(vocabulary_bigram).toarray()

        return vectorizer_bigram


############################
# NLP HELPER
############################
CUSTOM_STOPWORDS = ['i', 'me', 'up', 'my', 'myself', 'we', 'our', 'ours',
                    'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves',
                    'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself',
                    'it', 'its', 'itself', 'they', 'them', 'their', 'theirs',
                    'themselves', 'am', 'is', 'are', 'a', 'an', 'the', 'and', 'in', 'of', 'so',
                    'out', 'on', 'up', 'down', 's', 't', 'to', 'be', 'your', 'have', 'app', 'too']
KEYWORDS_BUG = "bug|crash|glitch|freeze|hang|not work|stop work|kill|dead|frustrate|froze|fix|close|error|gone|problem"
KEYWORDS_FEATURE_REQUEST = "should|wish|add|miss|lack|need"

l = nltk.WordNetLemmatizer()
t = nltk.RegexpTokenizer(r'[a-z]\w+')

cwd = os.getcwd()
print('PATH:', cwd)
print('files:', os.listdir('.'))

path_to_model = "stanford-postagger-full-2016-10-31/models/english-bidirectional-distsim.tagger"
path_to_jar = "stanford-postagger-full-2016-10-31/stanford-postagger.jar"
pos_tagger = nltk.StanfordPOSTagger(model_filename=path_to_model, path_to_jar=path_to_jar,
                                    java_options='-Xmx4060m -mx4060m')


class NLPHelper:
    @staticmethod
    def get_wordnet_pos(treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return 'a'

    @staticmethod
    def lem(sentence):
        tokens = t.tokenize(sentence)
        result = []
        for (token, tag) in nltk.pos_tag(tokens):
            result.append(l.lemmatize(token, NLPHelper.get_wordnet_pos(tag)))

        return " ".join(result)

    @staticmethod
    def remove_stopwords(text):
        return " ".join([w for w in text.split() if w not in CUSTOM_STOPWORDS])

    @staticmethod
    def pos_tag(text):
        return pos_tagger.tag(text)

    @staticmethod
    def extract_keyword_freq(feature="bug", text=""):
        if feature == "bug":
            return len(re.findall(KEYWORDS_BUG, text, re.IGNORECASE))
        elif feature == "feature":
            return len(re.findall(KEYWORDS_FEATURE_REQUEST, text, re.IGNORECASE))

    @staticmethod
    def extract_word_cont(text):
        return len(text.split())

    @staticmethod
    def count_tense_occurrences(review):
        tense = Tense()
        tokens = t.tokenize(review)
        pos_tagged = NLPHelper.pos_tag(tokens)

        for (token, pos_tag) in pos_tagged:
            if pos_tag in ["VB", "VBG", "VBP", "VBZ"]:
                tense.no_present += 1
            elif pos_tag in ["VBD", "VBN"]:
                tense.no_past += 1

            if token in ["will", "ll", "shall"]:
                tense.no_future += 1

        return tense

    @staticmethod
    def get_sentiment(review):
        DIR_ROOT = os.getcwd()
        senti_jar = os.path.join(DIR_ROOT, 'sentistrength/SentiStrength.jar')
        senti_folder = os.path.join(
            DIR_ROOT, 'sentistrength/SentStrength_Data/')
        p = subprocess.Popen(
            shlex.split('java -jar ' + senti_jar +
                        ' stdin sentidata ' + senti_folder),
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        # communicate via stdin the string to be rated. Note that all spaces are replaced with +
        stdout_text, stderr_text = p.communicate(
            bytearray(review.replace(" ", "+"), 'utf8'))
        p.kill()
        return str(stdout_text, 'utf-8').split()

    @staticmethod
    def get_sentiment_pos_score(sentiment_raw):
        return int(sentiment_raw[0])

    @staticmethod
    def get_sentiment_neg_score(sentiment_raw):
        return int(sentiment_raw[1])

    @staticmethod
    def get_sentiment_single_score(sentiment_raw):
        score_pos = int(sentiment_raw[0])
        score_neg = int(sentiment_raw[1])
        if abs(score_pos) > abs(score_neg):
            return score_pos
        elif abs(score_pos) == abs(score_neg):
            return 0
        else:
            return score_neg


class Tense:
    def __init__(self):
        self.no_present = 0
        self.no_past = 0
        self.no_future = 0
