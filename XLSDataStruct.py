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
        'on'
    ]
    punctuation = [
        '.',
        '!',
        '\"',
        '?',
        '/',
        '\\',
    ]

    def validate(self,item):

        v = str(item).lstrip('empty:').lstrip('text:').lstrip('ldate:').strip('\'')\
            .replace('\\n',' ')
        for word in self.filteredWords:
            v = v.replace(' '+word+' ',' ')
        for word in self.punctuation:
            v = v.replace(word,'')

        return v