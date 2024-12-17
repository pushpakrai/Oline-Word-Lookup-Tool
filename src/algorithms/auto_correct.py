class AutoCorrect:
    def __init__(self, words):
        self.words = set(words)

    def correct(self, word):
        if word in self.words:
            return word
        return min(self.words, key=lambda w: self._edit_distance(word, w))

    def _edit_distance(self, s1, s2):
        if len(s1) < len(s2):
            return self._edit_distance(s2, s1)
        if len(s2) == 0:
            return len(s1)
        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        return previous_row[-1]