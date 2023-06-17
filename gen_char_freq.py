from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords
import re
from collections import Counter
import pickle
import sys, os


def read_file(infile):
    if os.path.exists(infile) is False:
        print(f'Input file {infile} does not exists')
        return None
    fd = open(infile, encoding='utf=8')
    return fd


def filter_input(in_line):
    in_line = str(in_line)
    in_line = ''.join(c for c in in_line if ('\u0900' <= c <= '\u097f') or ('\u0000' <= c <= '\u007f'))
    in_line = in_line.replace('{html}', "")
    out_line = re.sub(r'http\S+', '', in_line)
    return out_line


def generate_char_freq_save_filtered(fd, viz, outfile):
    if os.path.exists(outfile) is True:
        os.remove(outfile)

    with open(outfile, 'a') as of:
        cntr = Counter()
        for item in fd:
            filtered = filter_input(item)
            cntr += Counter(filtered.strip())
            of.write(filtered)
    fd.close()

    freq = dict(cntr)
    total = sum(freq.values())
    norm_freq = {k: v / total for k, v in freq.items()}
    if viz is True:
        for k in sorted(norm_freq.items()):
            print(k)
    return norm_freq


def save_freq_model(freq_model):
    with open('char_freq.cp', 'wb') as f:
        pickle.dump(freq_model, f)


def start_main():
    if len(sys.argv) < 4:
        print(f'Usage: {sys.argv[0]} <path to input file> <path to output file> <visualize text frequency>')
        exit(0)
    infile = sys.argv[1]
    outfile = sys.argv[2]
    viz = bool(sys.argv[3])

    fd = read_file(infile)
    if fd is None:
        exit(-1)
    freq_model = generate_char_freq_save_filtered(fd, viz, outfile)
    save_freq_model(freq_model)


if __name__ == '__main__':
    start_main()
