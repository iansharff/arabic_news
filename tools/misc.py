import pickle
import requests
import nltk

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

PATTERN = r'[\u0621-\u064A]+'
STOPWORDS_URL = 'https://raw.githubusercontent.com/mohataher/arabic-stop-words/master/list.txt'
VALIDATION_SPLIT = 0.2
BATCH_SIZE = 10_000
SEED = 123
MAX_FEATURES = 10_000

CLASSES = [
    'Culture',
    'Finance',
    'Medical',
    'Politics',
    'Religion',
    'Sports',
    'Tech'
]

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