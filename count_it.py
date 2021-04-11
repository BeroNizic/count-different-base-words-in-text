# https://stackoverflow.com/questions/45403390/lemmatizing-italian-sentences-for-frequency-counting

import nltk
import string
import pattern
import json
import sys
from pattern.it import parse
from collections import Counter

# dictionary of Italian stop-words
it_stop_words = nltk.corpus.stopwords.words('italian')

# the following function is just to get the lemma
# out of the original input word (but right now
# it may be loosing the context about the sentence
# from where the word is coming from i.e.
# the same word could either be a noun/verb/adjective
# according to the context)
def lemmatize_word(input_word):
    in_word = input_word#.decode('utf-8')    
    word_it = parse(
        in_word, 
        tokenize=False,  
        tag=False,  
        chunk=False,  
        lemmata=True 
    )
    the_lemmatized_word = word_it.split()[0][0][4]    
    return the_lemmatized_word

def lemmatizeInputFile(inputFile, outputFile = "", mostFrequentNumber = 1000):
    with open(inputFile, 'r', encoding="utf-8") as myfile:
        it_string=myfile.read()
	
    # 1st tokenize the sentence(s)
    word_tokenized_list = nltk.tokenize.word_tokenize(it_string)
    # print("1) NLTK tokenizer, num words: {} for list: {}".format(len(word_tokenized_list), word_tokenized_list))

    # 2nd remove punctuation and everything lower case
    word_tokenized_no_punct = [str.lower(x) for x in word_tokenized_list if x not in string.punctuation]
    # print("2) Clean punctuation, num words: {} for list: {}".format(len(word_tokenized_no_punct), word_tokenized_no_punct))

    # 3rd remove stop words (for the Italian language)
    word_tokenized_no_punct_no_sw = [x for x in word_tokenized_no_punct if x not in it_stop_words]
    # print("3) Clean stop-words, num words: {} for list: {}".format(len(word_tokenized_no_punct_no_sw), word_tokenized_no_punct_no_sw))

    # 4.1 lemmatize the words
    word_tokenize_list_no_punct_lc_no_stowords_lemmatized = [lemmatize_word(x) for x in word_tokenized_no_punct_no_sw]
    #print("4.1) lemmatizer, num words: {} for list: {}".format(len(word_tokenize_list_no_punct_lc_no_stowords_lemmatized), word_tokenize_list_no_punct_lc_no_stowords_lemmatized))

    if (outputFile != ""):
        frequencies = Counter(word_tokenize_list_no_punct_lc_no_stowords_lemmatized)
        with open(outputFile, 'w', encoding="utf-8") as filehandle:
            for word, frequency in frequencies.most_common(mostFrequentNumber):  # get the most frequent words
                filehandle.write("{} {} \n".format(word, frequency))

    totalLemmas = len(word_tokenize_list_no_punct_lc_no_stowords_lemmatized)
    distinctLemmas = len(set(word_tokenize_list_no_punct_lc_no_stowords_lemmatized))
    variance = distinctLemmas / totalLemmas
    print("Distinct lemma words:", distinctLemmas, "Total number of lemma words:", totalLemmas, "Variance:", variance)

if __name__ == "__main__":
    inputFile = sys.argv[1]
    outputFile = sys.argv[2] if len(sys.argv) > 2 else ""
    mostFrequentNumber = int(sys.argv[3]) if len(sys.argv) > 3 else 1000
    lemmatizeInputFile(inputFile, outputFile, mostFrequentNumber)
