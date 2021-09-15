# -*- coding: utf-8 -*-
"""
This script produces a DataFrame and stores it as a pickle file to be used for initial model testing. Data needs to be present in repo to use
"""
import os
import pandas as pd

from tools import misc

ROOT_PATH = 'raw_data/sanad_subset'
TRAIN_SPLIT = 0.8
SEED = 42
PATTERN = r'[\u0621-\u064A]+'
STOPWORDS_URL = 'https://raw.githubusercontent.com/mohataher/arabic-stop-words/master/list.txt'

def main():
    print('-'*50)
    print('ROOT_PATH:',ROOT_PATH)
    print('TRAIN_SPLIT:', TRAIN_SPLIT)
    print('SEED:', SEED)
    print('-'*50)

    os.chdir(ROOT_PATH)
    print('from directory: ' + os.getcwd())

    cls_dict = {}
    corpus = []
    
    file_count = 0
    cls_counts = []

    dirnames = [d for d in os.listdir() if os.path.isdir(d)]
    for dirname in dirnames:
        dir_count = 0
        filepaths = [os.path.join(dirname, filename) for filename in os.listdir(dirname) if filename.endswith('.txt')]
        cls_dict[dirname] = filepaths

        for filepath in filepaths:
            f = open(filepath, 'r')
            text = f.read()
            f.close()

            docu = {'id': file_count, 'cls': dirname.lower(), 'text': text}
            corpus.append(docu)

            dir_count += 1
            file_count += 1
        cls_counts.append(dir_count)

    print(f"{file_count} files found belonging to {len(cls_counts)} classes:\n", end='\n\t')
    print(*[f"{dname}: {len(fnames)}" for dname, fnames in cls_dict.items()], sep='\n\t')
    
    corpus_df = pd.DataFrame(corpus).set_index('id')
    misc.save(corpus_df, 'corpus_df.pkl')


if __name__ == '__main__':
    main()
