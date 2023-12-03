# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, anagrams):
        sorted_word = sorted(self.word.lower())

        find_anagrams = [a for a in anagrams if sorted(a.lower()) == sorted_word and a.lower() != self.word.lower()]

        return find_anagrams