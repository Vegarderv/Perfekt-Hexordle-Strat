import sys

# PARAMS
NO_WORDS = 2
POS_MATTERS = True
FIRST_FIND_LETTERS = False

class PerfWordle:
    """Class for finding n perfect starting words"""
    def __init__(self) -> None:
        self.words = self._get_words()
        self.letter_dict = self._get_letter_dict()
        if not POS_MATTERS:
            self._remove_duplicates()
        if FIRST_FIND_LETTERS:
            self._firt_num_letters()

    
    def _firt_num_letters(self) -> None:
        most_important_letters = ""
        for i, key in enumerate(sorted(self.letter_dict, key=lambda x: sum(self.letter_dict[x]), reverse=True)):
            if i >= NO_WORDS * 5:
                break
            most_important_letters += key
        print(most_important_letters)
        new_words = []
        for word in self.words:
            in_word = True
            for letter in word:
                if letter not in most_important_letters:
                    in_word = False
                    break
            if in_word:
                new_words.append(word)
        self.words = new_words


    def _get_words(self) -> list[str]:
        with open("words.txt") as f:
            words = f.readlines()
        words = [word.strip() for word in words]
        return list(filter(lambda x: len(set(x)) == 5, words))  # Removing words with 2 of the same letter

    def _get_letter_dict(self) -> dict[str, list[int]]:
        letters = {
            #"a": [0, 0, 0, 0, 0],
            "b": [0, 0, 0, 0, 0],
            #"c": [0, 0, 0, 0, 0],
            #"d": [0, 0, 0, 0, 0],
            #"e": [0, 0, 0, 0, 0],
            "f": [0, 0, 0, 0, 0],
            "g": [0, 0, 0, 0, 0],
            "h": [0, 0, 0, 0, 0],
            #"i": [0, 0, 0, 0, 0],
            "j": [0, 0, 0, 0, 0],
            "k": [0, 0, 0, 0, 0],
            #"l": [0, 0, 0, 0, 0],
            #"m": [0, 0, 0, 0, 0],
            "n": [0, 0, 0, 0, 0],
            "o": [0, 0, 0, 0, 0],
            #"p": [0, 0, 0, 0, 0],
            "q": [0, 0, 0, 0, 0],
            #"r": [0, 0, 0, 0, 0],
            #"s": [0, 0, 0, 0, 0],
            "t": [0, 0, 0, 0, 0],
            #"u": [0, 0, 0, 0, 0],
            "v": [0, 0, 0, 0, 0],
            "w": [0, 0, 0, 0, 0],
            "x": [0, 0, 0, 0, 0],
            "y": [0, 0, 0, 0, 0],
            "z": [0, 0, 0, 0, 0],   
        }

        for word in self.words:
            for i, letter in enumerate(word):
                if letter not in letters:
                    continue
                letters[letter][i] += 1

        return letters
    
    def _remove_duplicates(self) -> None:
        no_duplicates = []
        duplicates_sorted = []
        for word in self.words:
            if sorted(word) not in duplicates_sorted:
                no_duplicates.append(word)
                duplicates_sorted.append(sorted(word))
            
        return no_duplicates
    
    def run(self) -> None:
        good_combos: dict[int, list[list[str]]] = {}

        length = len(self.words)

        

        i = 0
        while len(self.words):
            print('{:.1f}'.format(i / length * 100), "%", end="\r")
            word_list = ["" for _ in range(NO_WORDS)]
            word_list[0] = self.words[0]
            self._check_words(word_list[0], 1, good_combos, self.words, word_list)
            self.words.pop(0)
            i += 1
        
        myKeys = list(good_combos.keys())
        myKeys.sort()
        best_key = myKeys[-1]
        best_combos = good_combos[best_key]
        print(best_combos)
        
    def _get_score(self, word_list: list[str]) -> int:
        score = 0
        for word in word_list:
            for i, letter in enumerate(word):
                score += self.letter_dict[letter][i]
        return score
    
    def _check_words(self, word: str, depth: int, good_combos: dict[int, list[list[str]]], words: list[str], word_list: list[str]) -> None:
        filtered_words = list(filter(lambda x: len(set(word)&set(x)) == 0 and word != x, words))
        while len(filtered_words):
            word_list[depth] = filtered_words[0]
            word_list = [word if i <= depth else "" for i, word in enumerate(word_list)]
            filtered_words.pop(0)

            # If NO_WORDS is complete
            if depth == NO_WORDS - 1:
                score = self._get_score(word_list)
                if score not in good_combos:
                    good_combos[score] = []
                good_combos[score].append(word_list)
            
            else:
                self._check_words(word_list[depth], depth + 1, good_combos, filtered_words, word_list)
                











"""i = 0
for word in words:
    if i % 10 == 0:
        print(i)
    words2 = list(filter(lambda x: len(set(word)&set(x)) == 0 and word != x, words))
    for word2 in words2:
        words3 = list(filter(lambda x: len(set(word2)&set(x)) == 0 and word2 != x, words2))
        for word3 in words3:
            words4 = list(filter(lambda x: len(set(word3)&set(x)) == 0 and word3 != x, words3))
            for word4 in words4:
                combo = [word, word2, word3, word4]

                score = 0

                for w in combo:
                    for j, letter in enumerate(w):
                        score += letters[letter][j]
                
                if score not in good_combos.keys():
                    good_combos[score] = []
                good_combos[score].append(combo)
            words3 = words3[1:]
        words2 = words2[1:]
    words = words[1:]
    i += 1"""


if __name__ == "__main__":
    perf = PerfWordle()
    perf.run()





