import tensorflow as tf
from tensorflow.keras.preprocessing import text, text_dataset_from_directory

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier, Perceptron

from sklearn.feature_selection import RFECV
from sklearn.model_selection import GridSearchCV

from tools import misc
from tools import visualizations as vis

BATCH_SIZE = 32
VALIDATION_SPLIT = 0.2
SEED = 123

def main():
    pass

def get_dataset(path):
    return text_dataset_from_directory(
        directory=path,
        labels='inferred',
        batch_size=BATCH_SIZE,
        validation_split=VALIDATION_SPLIT
    )

def model_nb():
    pass



if __name__ == '__main__':
    main()
