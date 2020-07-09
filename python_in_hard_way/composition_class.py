"""
Write a program to show the function of composition in class.

"""


from parent_class import CalculateMean


class CompositeClass:

    def __init__(self):
        self.other=CalculateMean()

    def get_input(self):
        input=[5,10,15,20,56,45]
        return input

    def count_list(self,input):
        count=len(input)
        print(count)

    def print_result(self,input):
        mean=self.other.mean(input)
        print(mean)
        return mean

    def processes(self):
        input=self.get_input();
        self.count_list(input);
        self.print_result(input)


object=CompositeClass()
object.processes()

