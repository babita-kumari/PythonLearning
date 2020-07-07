"""
Write a program to calculate mean and standard deviation of given list.

"""
import math

from mean import CalculateMean


class CalculateSD(CalculateMean):

    def get_deviation(self, input_data, mean):
        deviation_list = []
        for number in inpugt_data:
            deviation = number - mean
            deviation_list.append(deviation)
        return deviation_list

    def get_deviation_square(self, deviation_list):
        square_deviation_list = []
        for number in deviation_list:
            square_of_deviation = number * number
            square_deviation_list.append(square_of_deviation)
        return square_deviation_list

    def calculate_sd(self, square_deviation_list, input_data):
        deviation = math.sqrt((sum(square_deviation_list) / len(input_data)))
        return deviation

    def print_result(self, deviation):
        print(deviation)

    def processes(self, input_data, mean):
        deviation = self.get_deviation(input_data, mean);
        deviation_square = self.get_deviation_square(deviation);
        standard_deviation = self.calculate_sd(deviation_square, input_data);
        self.print_result(standard_deviation)


number_object = CalculateSD()
input_data = number_object.get_input();
mean = number_object.calculate_mean(input_data)
number_object.processes(input_data, mean)
