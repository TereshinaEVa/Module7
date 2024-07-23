class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for word_key in self.file_names:
            one_str = ''
            with open(word_key, 'r+', encoding='utf-8') as file:
                to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for line in file:
                    one_str = one_str + (line.lower())
                for dell_simb in to_remove:
                   one_str = one_str.replace(dell_simb, '')
                one_str = one_str.split()
                all_words[word_key] = one_str
        return all_words

    def find(self, word):
        find_word = {}
        for name, words in (WordsFinder.get_all_words(self)).items():
            find_word[name] = words.index(word.lower()) + 1
        return find_word

    def count(self, word):
        find_word = {}
        for name, words in (WordsFinder.get_all_words(self)).items():
            find_word[name] = words.count(word.lower())
        return find_word



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
#print(finder2.file_names)