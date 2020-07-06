# Write a program that prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.

class UpperCaseConversion:

    #def __int__(self):
       # self.text=""

    def get_file(self):
        text=input('enter input:')
        content=open(text)
        mylist=content.read()
        return mylist

    def convert_upper(self,mylist):
        fh=mylist.upper()
        return fh

    def print_result(self,fh):
        print(fh)

    def processes(self):
        input=self.get_file()
        converted_file=self.convert_upper(input);
        self.print_result(converted_file)

f1= UpperCaseConversion()
f1.processes()


