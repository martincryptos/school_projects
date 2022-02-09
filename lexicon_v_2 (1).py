vocabulary = {
    'direction': 'north east west south up down left right back hoopla hippling'.split(),
    'noun': 'bear princess door cabinet'.split(),
    'stop': 'the in of from at it'.split(),
    'verb': 'go kill eat stop'.split(),
}

classifications = {i: k for k, v in vocabulary.iteritems() for i in v}

def classify(word):
    try:
        return 'number', int(word)
    except ValueError:
        return classifications.get(word, 'error'), word

def scan(words):
    return [classify(word.lower()) for word in words.split()]
