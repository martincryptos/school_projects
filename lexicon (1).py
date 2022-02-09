direction = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verb = ('go', 'stop', 'kill', 'eat')
stop = ('the', 'in', 'of', 'from', 'at', 'it')
noun = ('door', 'bear', 'princess', 'cabinet')
list1 = [direction, verb, stop, noun]

def scan(sentence):
    """This functin splits only arg, 'x' and classifies into tuples"""
    sentence = sentence.lower()
    words = sentence.split()
    stuff = []
    for word in words:
        if word in direction:
            stuff.append(('direction', word))
#        else:
#            pass
        elif word in verb:
            stuff.append(('verb', word))
#        else:
#            pass
        elif word in stop:
            stuff.append(('stop', word))
#        else:
#            pass
        elif word in noun:
            stuff.append(('noun', word))
#        else:
#            pass
        elif word.isdigit() is True:
            stuff.append(('number', int(word)))
        else:
#            pass
#        if word != [direction, verb, stop, noun] and word.isalpha():
            stuff.append(('error', word))
#        else:
#                                           pass
    return stuff
