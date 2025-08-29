# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # store lowercase for comparison

    def match(self, candidates):
        matches = []
        sorted_word = sorted(self.word)
        
        for candidate in candidates:
            if candidate.lower() != self.word and sorted(candidate.lower()) == sorted_word:
                matches.append(candidate)
        
        return matches
