"""
Write a program to calculate mean and standard deviation of given list.

"""
import math

class CalculateSD:

    def get_input(self):
        input=[10,12,45,69,78,56,23,45,76,56,85,24,29,65,91]
        return input

    def calculate_mean(self,input):
        mean=sum(input)/len(input)
        print(mean)
        return mean

    def get_deviation(self,input,mean):
        deviation_list=[]
        for number in input:
            deviation=number-mean
            deviation_list.append(deviation)
        return deviation_list

    def get_deviation_square(self,deviation_list):
        square_deviation_list=[]
        for number in deviation_list:
            square_of_deviation=number*number
            square_deviation_list.append(square_of_deviation)
        return square_deviation_list

    def calculate_sd(self,square_deviation_list,input):
        deviation=math.sqrt((sum(square_deviation_list)/len(input)))
        return deviation

    def print_result(self,deviation):
        print(deviation)

    def processes(self):
        input=self.get_input();
        mean=self.calculate_mean(input);
        deviation=self.get_deviation(input,mean);
        deviation_square=self.get_deviation_square(deviation);
        standard_deviation=self.calculate_sd(deviation_square,input);
        self.print_result(standard_deviation)

number_object=CalculateSD()
number_object.processes()



