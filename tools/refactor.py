import os
# Define encodings for sources and classes to assign to filenames
SOURCES = {
    'Akhbarona': 'ak',
    'Arabiya': 'ar',
    'Khaleej': 'kh'
}

CLASSES = {
    'Culture': 'c',
    'Finance': 'f',
    'Medical': 'm',
    'Politics': 'p',
    'Religion': 'r',
    'Sports': 's',
    'Tech': 't'
}

def main():
    """Combine .txt files from each Source into one directory to create Dataset generator object for batch training"""
    
    # Change working directory to full corpus directory
    os.chdir('./raw_data/sanad_full_copy')

    # Make directories for combined files if they don't exist
    for cls in CLASSES.keys():
        if not os.path.exists(cls):
            os.mkdir(cls)

    # Refactor files recursively with the format {dir_code}_{cls_code}_{i}.txt 
    for directory, dir_code in SOURCES.items():
        for cls_dir, cls_code in CLASSES.items():
            for i, filename in enumerate(os.listdir(os.path.join(directory, cls_dir))):
                os.rename(os.path.join(directory, cls_dir, filename), os.path.join(cls_dir, f'{dir_code}_{cls_code}_{i}.txt'))

if __name__ == '__main__':
    main()