class ParserError(Exception):
    pass

#class Sentence(ParserMethods):
#
#    def __init__(self, subject, verb, obj):
#        # remember we take ('noun', 'princess') tuples and convert them
#        self.subject = subject[1]
#        self.verb = verb[1]
#        self.object = obj[1]

class ParserMethods(object):

    def peek(self, word_list):
        if word_list:
            word = word_list[0]
            return word[0]
        else:
            return None

    def match(self, word_list, expecting):
        if word_list:
            word = word_list.pop(0)

            if word[0] == expecting:
                return word
            else:
                return None
        else:
            return None

    def skip(self, word_list, word_type):
        c = ParserMethods()
        while c.peek(word_list) == word_type:
            v = ParserMethods()
            v.match(word_list, word_type)

    def parse_verb(self, word_list):
        x = ParserMethods()
        x.skip(word_list, 'stop')

        if x.peek(word_list) == 'verb':
            return x.match(word_list, 'verb')
        else:
            return ParserError("Expected a verb next.")

    def parse_object(self, word_list):
        x = ParserMethods()
        x.skip(word_list, 'stop')
        next_word = x.peek(word_list)

        if next_word == 'noun':
            return x.match(word_list, 'noun')
        elif next_word == 'direction':
            return x.match(word_list, 'direction')
        else:
            return ParserError("Expected a noun or direction next.")

    def parse_subject(self, word_list):
        word_list = word_list
        x = ParserMethods()
        x.skip(word_list, 'stop')
        y = ParserMethods()
        next_word = y.peek(word_list)

        if next_word == 'noun':
            f = ParserMethods()
            return f.match(word_list, 'noun')
        elif next_word == 'verb':
            return ('noun', 'player')
        else:
            raise ParserError("Expected a verb next.")

class Sentence(object):

    def __init__(self, subject, verb, obj):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

def parse_sentence(word_list):
    x = ParserMethods()
    subj = x.parse_subject(word_list)
    c = subj
    y = ParserMethods()
    verb = y.parse_verb(word_list)
    h = verb
    v = ParserMethods()
    obj = v.parse_object(word_list)
    j = obj

    return Sentence(c, h, j)
