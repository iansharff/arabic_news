# -*- coding: utf-8 -*-
import numpy as np

import tensorflow as tf
from tensorflow.keras.preprocessing import text, text_dataset_from_directory

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier, Perceptron

from sklearn.feature_selection import RFECV

from tools import misc
from tools import visualizations as vis

def main():
    train_ds = get_dataset('raw_data/sanad_full_copy', 'training')
    val_ds = get_dataset('raw_data/sanad_full_copy', 'validation', batch_size=39034)

    nb_model = MultinomialNB()
    count_vectorizer = CountVectorizer(
        encoding = 'utf-8',
        strip_accents= 'unicode',
        lowercase=False,
        token_pattern = misc.PATTERN
    )
    for i, (text_batch, label_batch) in enumerate(train_ds):
        if i == 0:
            text_batch_cv = count_vectorizer.fit_transform(text_batch.numpy())
            nb_model.partial_fit(text_batch_cv, label_batch.numpy(), classes=np.arange(7))

        else:
            text_batch_cv = count_vectorizer.transform(text_batch.numpy())
            nb_model.partial_fit(text_batch_cv, label_batch.numpy())
        print(f"Batch {i+1}/{len(train_ds)} fitted")
    
    val_texts, val_labels = next(iter(val_ds))
    val_texts = val_texts.numpy()
    val_labels = val_labels.numpy()
    val_texts_cv = count_vectorizer.transform(val_texts)

    misc.save(nb_model, 'outputs/models/nb_full_train.pkl')
    misc.save(val_texts_cv, 'outputs/models/val_texts_cv.pkl')
    misc.save(val_labels, 'outputs/models/val_labels.pkl')
    misc.save(count_vectorizer, 'outputs/models/count_vectorizer.pkl')
        

def get_dataset(path, subset, batch_size=misc.BATCH_SIZE):
    return text_dataset_from_directory(
        directory=path,
        labels='inferred',
        label_mode='int',
        batch_size=misc.BATCH_SIZE,
        subset=subset,
        validation_split=misc.VALIDATION_SPLIT,
        seed=misc.SEED
    )


def model_nb():
    pass



if __name__ == '__main__':
    main()
