
"""
Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.

"""

class Income:

    def get_hours(self):
        hours=input("enter input:")
        h=float(hours)
        return h

    def get_rates(self):
        rates=input("enter input:")
        r=float(rates)
        return r

    def compute_pay(self,h,r):
        if h<40:
            net_pay=h*r
            return net_pay
        else:
            net_pay=h*r
            extra_pay=(h-40)*(r*0.5)
            net_pay=net_pay+extra_pay
        return net_pay

    def print_result(self,net_pay):
        print(net_pay)

    def processes(self):
        hours=self.get_hours();
        rates=self.get_rates();
        pay=self.compute_pay(hours,rates);
        self.print_result(pay)

employee1=Income()
employee1.processes()