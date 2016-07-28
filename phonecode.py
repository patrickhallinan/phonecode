#!/usr/bin/env python
import sys


WORD_FILENAME = sys.argv[1]
NUMBER_FILENAME = sys.argv[2]


# E | J N Q | R W X | D S Y | F T | A M | C I V | B K U | L O P | G H Z 
# e | j n q | r w x | d s y | f t | a m | c i v | b k u | l o p | g h z 
# 0 |   1   |   2   |   3   |  4  |  5  |   6   |   7   |   8   |   9 
 
letter_to_number_map = {}
letters = ('E', 'JNQ', 'RWX', 'DSY', 'FT', 'AM', 'CIV', 'BKU', 'LOP', 'GHZ')
for i, s in enumerate(letters):
    for c in s:
        letter_to_number_map[c] = i
        letter_to_number_map[c.lower()] = i

class Result:
    def __init__(self, word, numbers_left):
        self.word = word
        self.numbers_left = numbers_left

class Node:   
    def __init__(self):
        self.lookup = [None for i in range(10)]
        self.words = []
    
    def add_letter(self, c):
        if not c.isalpha():
            return self
        index = letter_to_number_map[c]
        node = self.lookup[index]
        if not node:
            node = Node()
            self.lookup[index] = node
        return node

class Phonecode:
        self.roots = [None for i in range(10)]

    def _find_words(self, number):
        results = []
        node = head
        for i in range(len(number)):
            c = number[i]
            if c.isdigit():
                node = node.lookup[int(c)]
                if not node:
                    break
                left = number[:i+1]
                right = number[i+1:]
                for word in node.words:
                    results.append(Result(left, right, word))
        return results

    def find_aliases(number):
        words_array = []

        results = self._find_words(number)
        if results:
            for result in results:

        else:
            if len(number) == 1:
                return [[number],]
            d = number[0]
            number = number[1:]
            results = self._find_words(number)

            if results:
                return []

        return words_array


if __name__ == '__main__':
    f = open(WORD_FILENAME)
    for line in f:
        word = line.strip()
        node = head
        for c in word:
            node = node.add_letter(c)
        node.words.append(word)
    f.close()
    
    f = open(NUMBER_FILENAME)
    for line in f:
        number = line.strip()
        words = []
        for word in find_aliases(number):
            print number, word
 
