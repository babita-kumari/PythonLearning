
class CalculateMean:

    def get_input(self):
        input = [10, 12, 45, 69, 78, 56, 23, 45, 76, 56, 85, 24, 29, 65, 91]
        return input


    def calculate_mean(self, input):
        mean = sum(input) / len(input)
        return mean

    def print_result(self,mean):
        print(mean)

    def processes(self):
        input=self.get_input();
        mean=self.calculate_mean(input);
        self.print_result(mean)

mean_object=CalculateMean()
mean_object.processes()