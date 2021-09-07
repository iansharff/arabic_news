import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.metrics import confusion_matrix
from tools import misc

FIG_KWS = {
    'family': 'serif',
    'size': 18,
    'weight': 'bold'
}

AX_KWS = {
    'family': 'serif',
    'size': 14
}

ANNOT_KWS = {
    'family': 'serif',
    'size': 10
}

def plot_confusion_matrices(model, X_train, X_test, y_train, y_test):
    
    y_hat_train = model.predict(X_train)
    y_hat_test = model.predict(X_test)

    cm_train = pd.DataFrame(confusion_matrix(y_train, y_hat_train)).rename(index=misc.CLASSES, columns=misc.CLASSES)
    cm_test = pd.DataFrame(confusion_matrix(y_test, y_hat_test)).rename(index=misc.CLASSES, columns=misc.CLASSES)

    fig, (ax_train, ax_test) = plt.subplots(1, 2, figsize=(15, 8))
    fig.suptitle(f'{model.steps[1][0]}', fontsize=18, fontweight='bold', fontdict=FIG_KWS)

    sns.heatmap(
        cm_train,
        ax=ax_train,
        annot=True,
        fmt='.0f',
        cmap='Greens',
        cbar=False
    )
    ax_train.set_title('Training', fontdict=AX_KWS)
    sns.heatmap(
        cm_test,
        ax=ax_test,
        annot=True,
        fmt='.0f',
        cmap='Reds',
        cbar=False
    )
    ax_test.set_title('Testing', fontdict=AX_KWS)

    return fig

def plot_clusters():
    pass

def word_map():
    pass
