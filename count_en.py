import nltk
import string
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk import word_tokenize, pos_tag
from collections import defaultdict, Counter
import sys

def lemmatizeInputFile(inputFile, outputFile = "", mostFrequentNumber = 1000):
    lmtzr = WordNetLemmatizer()

    en_stop_words = nltk.corpus.stopwords.words('english')
    tag_map = defaultdict(lambda: wn.NOUN)
    tag_map['J'] = wn.ADJ
    tag_map['V'] = wn.VERB
    tag_map['R'] = wn.ADV
    with open(inputFile, 'r' , encoding="latin-1") as myfile:
        data=myfile.read()

    word_tokenized_list = word_tokenize(data)
    word_tokenized_no_punct = [str.lower(x) for x in word_tokenized_list if x not in string.punctuation]

    word_tokenized_no_punct_no_sw = [x for x in word_tokenized_no_punct if x not in en_stop_words]

    word_tokenized_no_punct_no_sw_no_apostrophe = [x.split("'") for x in word_tokenized_no_punct_no_sw]
    word_tokenized_no_punct_no_sw_no_apostrophe = [y for x in word_tokenized_no_punct_no_sw_no_apostrophe for y in x]

    word_tokenize_list_no_punct_lc_no_stowords_lemmatized = []
    for token, tag in pos_tag(word_tokenized_no_punct_no_sw_no_apostrophe):
        lemma = lmtzr.lemmatize(token, tag_map[tag[0]])
        word_tokenize_list_no_punct_lc_no_stowords_lemmatized.append(lemma)
    
    if (outputFile != ""):
        frequencies = Counter(word_tokenize_list_no_punct_lc_no_stowords_lemmatized)
        with open(outputFile, 'w', encoding="utf-8") as filehandle:
            for word, frequency in frequencies.most_common(mostFrequentNumber):  # get the most frequent words
                filehandle.write("{} {} \n".format(word, frequency))

    totalLemmas = len(word_tokenize_list_no_punct_lc_no_stowords_lemmatized)
    distinctLemmas = len(set(word_tokenize_list_no_punct_lc_no_stowords_lemmatized))
    variance = distinctLemmas / totalLemmas
    print("Distinct lemma words:", distinctLemmas, "Total number of lemma words:", totalLemmas, "Variance:", variance)
    return word_tokenize_list_no_punct_lc_no_stowords_lemmatized

if __name__ == "__main__":
    inputFile = sys.argv[1]
    outputFile = sys.argv[2] if len(sys.argv) > 2 else ""
    mostFrequentNumber = int(sys.argv[3]) if len(sys.argv) > 3 else 1000
    lemmatizeInputFile(inputFile, outputFile, mostFrequentNumber)