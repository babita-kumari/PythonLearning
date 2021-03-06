"""
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number
of times they appear in the file. After the dictionary is produced,
the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

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



