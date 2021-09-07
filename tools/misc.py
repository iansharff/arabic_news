import pickle
import requests
import nltk

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

PATTERN = r'[\u0621-\u064A]+'
STOPWORDS_URL = 'https://raw.githubusercontent.com/mohataher/arabic-stop-words/master/list.txt'
TEST_SIZE = 0.2
SEED = 123
CLASSES = {
    0: 'culture',
    1: 'finance',
    2: 'medical',
    3: 'politics',
    4: 'religion',
    5: 'sports',
    6: 'tech'
}

def save(obj, filepath):
    """Save an object to a certain filepath"""
    f = open(filepath, 'wb')
    pickle.dump(obj, f)
    f.close()

def load(filepath):
    """Load .pkl file located at 'filepath'"""
    f = open(filepath, 'rb')
    obj = pickle.load(f)
    f.close()
    return obj

def get_stopwords(url = STOPWORDS_URL):
    r = requests.get(STOPWORDS_URL)
    stopwords = []
    if r.status_code:
        stopwords = r.text.split('\n')
    else:
        stopwords = nltk.corpus.stopwords.words('arabic')
    return stopwords