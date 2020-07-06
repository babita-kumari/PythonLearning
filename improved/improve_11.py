
"""
Write a programme to read through and parse a file with text and numbers and extract all the numbers in the file and compute the sum of the numbers.

step 1: read through and parse a file with text and numbers.
step 2: extract all the numbers in the file
step 3: convert the string into int
step 4: compute the sum of the numbers
"""


class ParseNumberAndSum:

    def __init__(self):
        self.global_number_list=[]

    def get_input(self):
        file_name=input("enter file name:")
        global_line=open(file_name)
        return global_line

    def find_number(self, global_line):
        import re
        for line in global_line:
            line=line.rstrip()
            numbers=re.findall('[0-9]+', line)
            for number in numbers:
                self.global_number_list.append(int(number))
        return self.global_number_list

    def calculate_count(self):
        count=len(self.global_number_list)
        return count

    def calulate_sum(self):
        total=sum(self.global_number_list)
        return total

    def print_result(self,total,count):
        print(total,count)

    def processes(self):
        input=self.get_input();
        number=self.find_number(input);
        count=self.calculate_count();
        total=self.calulate_sum();
        self.print_result(total,count)

object=ParseNumberAndSum()
object.processes()


#361152255063091 328066

