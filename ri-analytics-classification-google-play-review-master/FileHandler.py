import pickle

class PickleHandler:

    @staticmethod
    def load_ml_model(name=""):
        path = name + ".pickle"
        file = open(path, "rb")
        model = pickle.load(file)
        file.close()

        return model

    @staticmethod
    def load_vocabulary(name):
        path = "vocabulary_" + name + ".pickle"
        file = open(path, "rb")
        model = pickle.load(file)
        file.close()

        return model
