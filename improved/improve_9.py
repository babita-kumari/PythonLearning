class EmailParse:
    def __init__(self):
        self.email_dict={}

    def get_file(self):
        file_name=input("enter file name:")
        global_file=open(file_name)
        return global_file

    def get_words(self, global_file):
        global_word_list=[]
        for line in global_file:
            if line.startswith ("From "):
                words = line.split()
                email_id = words[1]
                global_word_list.append(email_id)
        return global_word_list

    def store_in_dictionary(self, global_word_list):
        for word in global_word_list:
            self.email_dict[word]=self.email_dict.get(word,0)+1
        return self.email_dict

    def get_maxcount_max_email(self):
        maxcount=None
        max_email=None
        for email,count in self.email_dict.items():
            if maxcount is None or count > maxcount:
                max_email=email
                maxcount=count
        print(max_email,maxcount)

    def processes(self):
        file=self.get_file();
        words=self.get_words(file);
        self.store_in_dictionary(words);
        self.get_maxcount_max_email()

email_list=EmailParse()
email_list.processes()



