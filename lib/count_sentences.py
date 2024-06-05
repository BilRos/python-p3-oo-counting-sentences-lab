#!/usr/bin/env python3
import re

class MyString:

    def __init__ (self,value = ""):
        self.value=value
      
    @property
    def control_value(self):
        return self._value

    @control_value.setter
    def control_value(self, control_value):
        if isinstance(control_value,str):
            self._value=control_value
        else:
            print ('The value must be a string.')


    def is_sentence(self):
        return True if self.value.endswith (".") else False

    def is_question():
        return True if self.value.endswith ("?") else False

    def is_exaclamation():
        return True if self.value.endswith ("!") else False

    def count_sentences():
        sentences = re.split(r'[.!?]', self.value)

        sentences = [value for value in sentences if value.strip()]
        return len(sentences)