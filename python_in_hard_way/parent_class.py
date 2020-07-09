class CalculateMean:

    def get_input(self):
        number_list=[2,5,6,7,8,9,45,46,87]
        return number_list

    def mean(self,number_list):
        mean=sum(number_list)/len(number_list)
        #print(mean)
        return mean

    def processes(self):
        input=self.get_input();
        self.mean(input)

mean1=CalculateMean()
mean1.processes()