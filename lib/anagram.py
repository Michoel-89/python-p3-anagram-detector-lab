# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, arr):
        lis = []
        for w in arr:
            array = list(w)
            array2 = list(self.word)
            if sorted(array) == sorted(array2):
                lis.append(''.join(array))
        return lis
