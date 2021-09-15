# -*- coding: utf-8 -*-
"""
This script when run will train a Naive Bayes Classifier with batches loaded in from the full corpus of 200,000 articles. In order to function, the
data must be present in the repository, with articles in directories separated by class.
"""
import numpy as np
from tensorflow.keras.preprocessing import text_dataset_from_directory
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from tools import misc

def main():
    """Train the final model on the full corpus in batches"""
    # Create Dataset iterators
    train_ds = get_dataset('raw_data/sanad_full_copy', 'training')
    val_ds = get_dataset('raw_data/sanad_full_copy', 'validation', batch_size=39034)

    # Instantiate model and CountVectorizer
    nb_model = MultinomialNB()
    count_vectorizer = CountVectorizer(
        encoding = 'utf-8',
        strip_accents= 'unicode',
        lowercase=False,
        max_df=0.5,
        token_pattern = misc.PATTERN
    )

    # Iterate through batches, fit vectorizer to first batch, and just transform the rest
    for i, (text_batch, label_batch) in enumerate(train_ds):
        if i == 0:
            text_batch_cv = count_vectorizer.fit_transform(text_batch.numpy())
            nb_model.partial_fit(text_batch_cv, label_batch.numpy(), classes=np.arange(7))

        else:
            text_batch_cv = count_vectorizer.transform(text_batch.numpy())
            nb_model.partial_fit(text_batch_cv, label_batch.numpy())
        print(f"Batch {i+1}/{len(train_ds)} fitted")
    
    # Count vectorize validation data
    val_texts, val_labels = next(iter(val_ds))
    val_texts = val_texts.numpy()
    val_labels = val_labels.numpy()
    val_texts_cv = count_vectorizer.transform(val_texts)

    # Save model and validation data to two locations
    misc.save(nb_model, 'outputs/models/nb_full_train.pkl')
    misc.save(nb_model, 'outputs/final_models/nb_full_train.pkl')

    misc.save(val_texts_cv, 'outputs/models/val_texts_cv.pkl')
    misc.save(val_texts_cv, 'outputs/final_models/val_texts_cv.pkl')

    misc.save(val_labels, 'outputs/models/val_labels.pkl')
    misc.save(val_labels, 'outputs/final_models/val_labels.pkl')

    misc.save(count_vectorizer, 'outputs/models/count_vectorizer.pkl')
        

def get_dataset(path, subset, batch_size=misc.BATCH_SIZE):
    """
    Create a tf.Dataset object to load batches of text data
    
    params:
        path: str, path to the data directory
        subset: str, 'training', or 'validation'
        batch_size: int, number of text files per batch, default is 10_000, found in misc.py
    """
    return text_dataset_from_directory(
        directory=path,
        labels='inferred',
        label_mode='int',
        batch_size=batch_size,
        subset=subset,
        validation_split=misc.VALIDATION_SPLIT,
        seed=misc.SEED
    )


if __name__ == '__main__':
    main()
