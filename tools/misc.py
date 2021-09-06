import pickle

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
