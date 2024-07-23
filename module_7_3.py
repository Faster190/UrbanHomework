class WordsFinder:
    def __init__(self, *names):
        self.file_names = names

    def get_all_words(self):
        all_words = {}
        for names in self.file_names:
            list_ = []
            with (open(names, encoding="utf-8") as file):
                for line in file:
                    str_ = line.lower()
                    str_ = str_.replace(',', '')
                    str_ = str_.replace('.', '')
                    str_ = str_.replace('!', '')
                    str_ = str_.replace('?', '')
                    str_ = str_.replace(';', '')
                    str_ = str_.replace(':', '')
                    str_ = str_.replace('=', ' ')
                    str_ = str_.replace(" - ", ' ')
                    tmp = str_.split()
                    for j in tmp:
                        list_.append(j)
            all_words[names] = list_
        return all_words

    def find(self, word):
        dict_ = {}
        all_words = self.get_all_words()
        for item in all_words.items():
            for j in range(len(item[1])):
                if item[1][j] == word.lower():
                    dict_[item[0]] = j + 1
                    break
        return dict_

    def count(self, word):
        dict_ = {}
        all_words = self.get_all_words()
        for item in all_words.items():
            ctr = 0
            for words in item[1]:
                if words == word.lower():
                    ctr += 1
            dict_[item[0]] = ctr
        return dict_


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
