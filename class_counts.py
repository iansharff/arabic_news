import os
import sys

def main():
    text_file = open('class_counts.txt', 'wt')
    sys.stdout = text_file
    orig_dir = os.curdir
    os.chdir('./raw_data')
    sources = os.listdir('./sanad_full')
    source_counts = {}
    totals = {}

    for source in sources:
        cat_counts = {}
        cats = [cat for cat in os.listdir(os.path.join('./sanad_full', source)) if os.path.isdir(cat)]
        for cat in cats:
            cat_count = len(os.listdir(os.path.join('./sanad_full', source, cat)))
            cat_counts[cat] = cat_count
            totals[cat] = totals.get(cat, 0) + cat_count
        source_counts[source] = cat_counts
    os.chdir(orig_dir)
    
    print("SANAD Class Counts")
    line()
    print(f"{sum(totals.values())} articles belonging to {len(totals)} classes")
    line()
    for source, cats in source_counts.items():
        print(source)
        line()
        for cat, count in cats.items():
            print(f"\t{cat}: {count}")
        line()
    print("TOTALS")
    line()
    for cat, total in totals.items():
        print(f'\t{cat}: {total}')
    line()

def line():
    print('-'*30)

if __name__ == '__main__':
    main()