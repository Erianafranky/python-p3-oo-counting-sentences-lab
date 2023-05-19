#!/usr/bin/env python3

#MyString prints "The value must be a string."
class MyString:
    def __init__(self, value= ""):
        self.value = value
    
    def get_value(self):
        return self._value
    
    def set_value(self, value):
        if type(value) is str:
            self._value = value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    #returns True if value ends with a period and False otherwise.
    def is_sentence(self):
        if self.value.endswith("."):
            return True
        else:
            return False

    #returns True if value ends with a question mark and False otherwise.    
    def is_question(self):
        if self.value.endswith("?"):
            return True
        else:
            return False

    #returns True if value ends with an exclamation mark and False if otherwise    
    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        else:
            return False

    #returns the number of sentences in the value.    
    def count_sentences(self):
        counter = 0
        sentences = self._value.split(' ')
        for sentence in sentences:
            string = MyString(sentence)
            if string.is_sentence() or string.is_question() or string.is_exclamation():
                counter += 1
        return counter
