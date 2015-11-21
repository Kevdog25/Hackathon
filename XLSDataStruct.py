import re
__author__ = 'Kevin'


class DataStruct:
    filteredWords = [
        'the',
        'be',
        'and',
        'of',
        'a',
        'to',
        'it',
        'for',
        'in',
        'an',
        'on',
        'my',
        'your',
        'is',
        'with',
        'at',
        'as',
        'from',
        'by',
        'with',
        'or',
        'you',
        'our',
        'we',
        '*',
        'will',
        'are',
    ]

    punctuation = [
        '.',
        ':',
        '!',
        '\"',
        '?',
        '/',
        '(',
        ')',
        '{',
        '}',
        '-',
        '\'s'
    ]

    def validate(self, item,splitAt = ' '):
        """Validates the input to reformat and remove unwanted characters and words"""
        v = str(item).lower().lstrip('empty:').lstrip('text:').lstrip('ldate:').strip('\'')
        v = re.sub('\\\\n', ' ', v)
        for word in self.filteredWords:
            v = v.replace(' '+word+' ', ' ')
        for word in self.punctuation:
            v = v.replace(word, '')
        v = re.sub('[ ]{2,}', ' ', v)
        v = re.sub(' [0-9]* ', ' ', v)
        v = re.sub('\&',' ', v)

        encoded = v.encode('ascii', 'ignore')
        return encoded.decode().split(splitAt)

    @staticmethod
    def countfrequency(s, f=None):
        if f is None:
            f = {}
        for w in s:
            w = w.strip(' ').strip(',').strip(';')
            if w in f.keys():
                f[w] += 1
            else:
                f[w] = 1

        return f

    @staticmethod
    def norm(thing):
        tot = 0
        for item in thing:
            tot += float(item[1])
        for i in range(len(thing)):
            thing[i][1] /= tot

    @staticmethod
    def compare(f1, f2):
        c = 0
        for k in f1.keys():
            if k in f2.keys():
                c += f2[k]*f1[k]
        return c

    @staticmethod
    def catfrequencies(f1, f2):
        for k in f2.keys():
            if k in f1.keys():
                f1[k] += f2[k]
            else:
                f1[k] = f2[k]
