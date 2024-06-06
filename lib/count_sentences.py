#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print('The value must be a string.')
    def is_sentence(self):
        return self.value[-1] == "."
    def is_question(self):
        return self.value[-1] == "?"
    def is_exclamation(self):
        return self.value[-1] == "!"
    def count_sentences(self):
        # count = self.value.count('.') + self.value.count('?') + self.value.count('!')
        newValue = self.value.replace('?', '.').replace('!', '.')
        l = newValue.split('.')
        count = 0
        for item in l:
            if len(item) != 0:
                count += 1
        return count
        
s = MyString('This, well, is a sentence. This is too!! And so is this, I think? Woo...')
print(s.is_sentence())
print(s.count_sentences())