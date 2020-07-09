from parent_class import CalculateMean


class CalculateMedian(CalculateMean):

    def get_input(self):
        number_list=[4,5,7,8,9,52,17,69,35,25,34]
        sorted_number=sorted(number_list)
        return sorted_number

    def calculate_median(self,sorted_number):
        for number in sorted_number:
            total=sum(sorted_number)
            n=len(sorted_number)+1
            median=total/n
        return median

    def print_result(self,median,mean):
        print(median,mean)

    def processes(self):
        input=self.get_input();
        median=self.calculate_median(input);
        mean=self.mean(input)
        self.print_result(median,mean)

number_object=CalculateMedian()
number_object.processes()



