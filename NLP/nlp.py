'''
Created on 14-Oct-2018

@author: 34320
'''
===============================================================================
Import Nltk and download packages 
===============================================================================

===============================================================================
import nltk
nltk.download()
===============================================================================

===============================================================================
Tokenize sentences and words
===============================================================================

===============================================================================
===============================================================================
from nltk.tokenize import sent_tokenize, word_tokenize
EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
print(sent_tokenize(EXAMPLE_TEXT))
===============================================================================
===============================================================================

===============================================================================
Using Python to tokenize without use of nltk
===============================================================================
===============================================================================

import urllib.request
response = urllib.request.urlopen('http://php.net/')
html = response.read()
print (html)
===============================================================================

===============================================================================
Get only Text ignoring tags 
===============================================================================

===============================================================================
Tokenizing a website data using simple python
===============================================================================

===============================================================================
from bs4 import BeautifulSoup
import urllib.request
response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
#print (text)
 
tokens = [t for t in text.split()]
print (tokens)
===============================================================================

===============================================================================
Frequency Distribution on NLTK
===============================================================================
Frequeuncy distrib

===============================================================================
freq = nltk.FreqDist(tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
     
freq.plot(20, cumulative=False)   
===============================================================================

===============================================================================
Removing Stop Words
===============================================================================
Removing Stop Words
===============================================================================
from nltk.corpus import stopwords
stopwords.words('english')

clean_tokens = tokens[:]
sr = stopwords.words('english')

for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
    
freq.plot(20, cumulative=False)
===============================================================================

===============================================================================
Tokenizing
===============================================================================
tokeninizing words using nltk
===============================================================================
from nltk.tokenize import sent_tokenize
mytext = "Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
print(sent_tokenize(mytext))
===============================================================================
===============================================================================
Tokenizing words 
===============================================================================
===============================================================================
from nltk.tokenize import word_tokenize
print(word_tokenize(mytext))
===============================================================================


===============================================================================
 Removing Stop words
===============================================================================

stop words simple example

===============================================================================
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)
===============================================================================


===============================================================================
#Port steemmer 
===============================================================================

===============================================================================
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps = PorterStemmer()
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
for w in example_words:
    print(ps.stem(w))

new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(new_text)
for w in words:
    print(ps.stem(w))
===============================================================================


===============================================================================
Synonyms and Antonyms
===============================================================================

wordnet has to be downloaded
Getting similar words
===============================================================================
nltk.download()
from nltk.corpus import wordnet
===============================================================================
===============================================================================

synonyms = []
syn = wordnet.synsets("pain")
print(syn[0].definition())
print(syn[0].examples())
print(synonyms)


from nltk.corpus import wordnet
synonyms = []
for syn in wordnet.synsets('Computer'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

from nltk.corpus import wordnet
antonyms = []
for syn in wordnet.synsets("small"):
    for l in syn.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(antonyms)
===============================================================================

===============================================================================
Parts of Speech Taggeing
===============================================================================

===============================================================================
One of the more powerful aspects of the NLTK module is the Part of Speech tagging that it can do for you.
This means labeling words in a sentence as nouns, adjectives, verbs...etc. Even more impressive, it also labels by tense, and more. Here's a list of the tags, what they mean, and some examples:
===============================================================================


===============================================================================
POS tag list:

CC    coordinating conjunction
CD    cardinal digit
DT    determiner
EX    existential there (like: "there is" ... think of it like "there exists")
FW    foreign word
IN    preposition/subordinating conjunction
JJ    adjective    'big'
JJR    adjective, comparative    'bigger'
JJS    adjective, superlative    'biggest'
LS    list marker    1)
MD    modal    could, will
NN    noun, singular 'desk'
NNS    noun plural    'desks'
NNP    proper noun, singular    'Harrison'
NNPS    proper noun, plural    'Americans'
PDT    predeterminer    'all the kids'
POS    possessive ending    parent\'s
PRP    personal pronoun    I, he, she
PRP$    possessive pronoun    my, his, hers
RB    adverb    very, silently,
RBR    adverb, comparative    better
RBS    adverb, superlative    best
RP    particle    give up
TO    to    go 'to' the store.
UH    interjection    errrrrrrrm
VB    verb, base form    take
VBD    verb, past tense    took
VBG    verb, gerund/present participle    taking
VBN    verb, past participle    taken
VBP    verb, sing. present, non-3d    take
VBZ    verb, 3rd person sing. present    takes
WDT    wh-determiner    which
WP    wh-pronoun    who, what
WP$    possessive wh-pronoun    whose
WRB    wh-abverb    where, when
===============================================================================


===============================================================================
Grouping Words /Chunking Grouping Nouns with words in relation to them
===============================================================================

===============================================================================
===============================================================================
Some Regex expressions
===============================================================================
+ = match 1 or more
? = match 0 or 1 repetitions.
* = match 0 or MORE repetitions      
. = Any character except a new line
===============================================================================

===============================================================================
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))


process_content()
===============================================================================

===============================================================================
Chunking after POS taggign
===============================================================================

===============================================================================
===============================================================================
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            
            print(chunked)
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print(subtree)

            chunked.draw()

    except Exception as e:
        print(str(e))

process_content()

===============================================================================
Process Content using chinking, filter unwanted words that are not removed in chunking
===============================================================================
===============================================================================

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            chunkGram = r"""Chunk: {<.*>+}
                                    }<VB.?|IN|DT|TO>+{"""

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            chunked.draw()

    except Exception as e:
        print(str(e))

process_content()
===============================================================================

===============================================================================
Identifying Named Entity
===============================================================================

===============================================================================
One of the most major forms of chunking in natural language processing is called "Named Entity Recognition." 

The idea is to have the machine immediately be able to pull out "entities" like people,
places, things, locations, monetary figures, and more.
===============================================================================

===============================================================================
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=True)
            namedEnt.draw()
    except Exception as e:
        print(str(e))


process_content()
===============================================================================

===============================================================================
Lemmatizing with nltk 
===============================================================================

===============================================================================
Lemmatizing Creates actual words 
===============================================================================
===============================================================================
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run",'v'))
===============================================================================

