"""
step1: open file and read line byline
step2: split the line which starts with from
step3:print out second word in the line
step4: print total count of the item in the list at the end
"""
class ParseEmail:

    def __init__(self):
        self.global_word_list=[]

    def get_file(self):
        file_name=input("enter file name:")
        global_file=open(file_name)
        return global_file

    def get_words(self, global_file):
        for line in global_file:
            if line.startswith("From "):
                words=line.split()
                email_id = words[1]
                self.global_word_list.append(email_id)

    def get_count(self):
        count = len(self.global_word_list)
        return count

    def print_words(self):
        for word in self.global_word_list:
            print(word)

    def print_result(self,count):
        print("There were", count, "lines in the file with From as the first word")

    def processes(self):
        file=self.get_file();
        words=self.get_words(file);
        count=self.get_count();
        self.print_words();
        self.print_result(count)

email_list=ParseEmail()
email_list.processes()




