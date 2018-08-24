import unidecode

#import nltk
#from nltk.corpus import cess_esp as cess

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')


def removeNonWords(line):
    line = ''.join(e for e in line if e.isalnum() or e.isspace())
    return line

def normalizeChars(line):
    line = unidecode.unidecode(line)
    line = line.lower()
    return line

def removeStopWords(line):
    stopwords = ['el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'por', 'que', 'es']
    querywords = line.split()
    resultwords = [word for word in querywords if word.lower() not in stopwords]
    return ' '.join(resultwords)

# open file
file = open("sentences.txt")

# read lines
lines = file.readlines()

for x in lines:
    x = removeNonWords(x)
    x = normalizeChars(x)
    x = removeStopWords(x)
    print (x)



# tokens
#tokens = nltk.word_tokenize(sentence)

# tags
#tags = nltk.pos_tag(tokens)

# entities
#entities = nltk.chunk.ne_chunk(tags)


