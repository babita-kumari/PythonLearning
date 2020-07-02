"""
    Step-0: Define global words_list
    Step-1: Read file line by line
    Step-2: Split each line into words
    Step-3: Append into global_word_list if words in word is not duplicate
    Step-4: Sort global_word_list
    Step-5: Print global word list
"""
class WordList:

    def __init__(self):
        self.word_list=[]

    def get_input(self):
        file_name = input("Enter file name: ")
        file = open(file_name)
        return file


    def split_text(self,file):
        words_in_file = []
        for line in file:
            line=line.rstrip()
            words=line.split()
            for word in words:
                words_in_file.append(word.upper())
        return words_in_file

    def remove_duplicate_word(self, words_in_file):
        #word_list=[]
        for word in words_in_file:
            if word in self.word_list:
                continue
            else:
                self.word_list.append(word)
        return self.word_list

    def sort_word(self):
        self.word_list.sort()
        return self.word_list

    def print_result(self):
        print(self.word_list)

    def processes(self):
        file_name=self.get_input();
        words=self.split_text(file_name);
        print(words);
        non_duplicate_words=self.remove_duplicate_word(words);
        print(non_duplicate_words);
        self.sort_word();
        self.print_result()

document=WordList()

document.processes()
