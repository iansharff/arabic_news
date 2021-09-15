import os

import pickle
import requests
import nltk
from pprint import pprint

from sklearn.model_selection import GridSearchCV

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
    """Obtain stopwords from either the source on GitHub or the NLTK default stopword list for Arabic"""
    r = requests.get(STOPWORDS_URL)
    stopwords = []
    if r.status_code:
        stopwords = r.text.split('\n')
    else:
        stopwords = nltk.corpus.stopwords.words('arabic')
    return stopwords

def get_absolute_paths(directory):
    """Get a list of absolute filepaths within a directory recursively"""
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            yield os.path.abspath(os.path.join(dirpath, filename))

def run_grid_search(X_train, y_train, pipeline, param_grid):
    """Run a grid search, provided data, labels, a pipeline with an estimator, and a parameter grid"""
    grid_search = GridSearchCV(pipeline, param_grid, n_jobs=-1, verbose=1)
    
    print("Grid Searching...")
    print("PIPELINE:")
    print(*[f'\t{name}' for name, _ in pipeline.steps], sep='\n')
    print("PARAMS:")
    pprint(param_grid)
    print()
    
    grid_search.fit(X_train, y_train)
    print(f'Best score: {grid_search.best_score_}')
    print("Best parameters:")
    best_estimator = grid_search.best_estimator_
    pprint(best_estimator.get_params())
    return best_estimator