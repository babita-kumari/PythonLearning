class ParseText:

    #def __init__(self,text):
        #self.text=text

    def get_text(self):
        text="X-DSPAM-Confidence:    0.8475"
        return text

    def find_index (self,text):
        result1=text.find(':')
        result2=text[result1+1:]
        result3=float(result2.lstrip())
        return result3

    def print_result(self, result3):
        print (result3)

    def processes(self):
        text=self.get_text();
        result4=self.find_index(text);
        self.print_result(result4)

c1=ParseText()
c1.processes()

