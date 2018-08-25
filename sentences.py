import unidecode
import pprint

import nltk
#from nltk.corpus import cess_esp as cess

#nltk.download('punkt')
#nltk.download('averaged_perceptron_taagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')


def removeNonWords(line):
    line = ''.join(e for e in line if e.isalnum() or e.isspace())
    return line

def normalizeChars(line):
    line = unidecode.unidecode(line)
    line = line.lower()
    return line

def removeStopWords(stopWords, line):
    querywords = line.split()
    resultwords = [word for word in querywords if word.lower() not in stopWords]
    return ' '.join(resultwords)

def sortedChunks(list, n):
    for i in range(0, len(list) - n, 1):
        yield ' '.join(sorted(list[i:i + n]))

def chunks(list, n):
    for i in range(0, len(list) - n, 1):
        yield ' '.join(list[i:i + n])

def sortingCount(value):
    return value

def dropValues(items, max):
    result = dict(items)
    for key, value in items.items():
        if value <= max:
            del result[key]
    return result

def sortByValue(items, reverse):
    return sorted(items.items(), key=lambda x: x[1], reverse=reverse)

def appendStats(stats, detail, words, line, count):
    sortedPhrases = list(sortedChunks(words, count))
    phrases = list(chunks(words, count))
    key=0
    for phrase in sortedPhrases:
        if phrase in stats:
            stats[phrase] += 1
            detail[phrase]['questions'].append(line)
            detail[phrase]['words'].append(phrases[key])
        else:
            stats[phrase] = 1
            detail[phrase] = {}
            detail[phrase]['questions'] = [line]
            detail[phrase]['words'] = [phrases[key]]
        key+=1

    return stats

# open file and read lines
file = open("sentences.txt")
# lines = file.readlines()
lines = file.read().splitlines()

file = open("stopwords-en.txt")
stopWords = file.read().splitlines()

phrases = {}
details= {}

for line in lines:
    #tokens = nltk.word_tokenize(x)
    #tags = nltk.pos_tag(tokens)
    tmp = removeNonWords(line)
    tmp = normalizeChars(tmp)
    tmp = removeStopWords(stopWords,tmp)
    words = tmp.split()
    phrases = appendStats(phrases, details, words, line,  3)
    phrases = appendStats(phrases, details, words, line, 4)

phrases = dropValues(phrases, 2)

sortedPhrases = sortByValue(phrases, reverse=True)

#pprint.pprint(sortedPhrases)

for key, value in sortedPhrases:
    words = details[key]['words'][0]
    print("\n[" + words + "] " + str(value) + " ocurrences:" )
    for line in details[key]['questions']:
        print(line)










# tokens
#tokens = nltk.word_tokenize(sentence)

# tags
#tags = nltk.pos_tag(tokens)

# entities
#entities = nltk.chunk.ne_chunk(tags)


