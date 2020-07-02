class Income:
    def __init__(self,hours,rates):
        self.hours=hours
        self.rates=rates

    def computepay(self,hours,rates):
        if hours<40:
            net_pay=self.hours*self.rates
            return net_pay
        else:
            net_pay=self.hours*self.rates
            extra_pay=(self.hours-40)*(self.rates*0.5)
            net_pay=net_pay+extra_pay
        return net_pay

employee1=Income(45,200)
print(employee1.computepay(45,200))