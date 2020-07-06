#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered,print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.


class FindLargestAndSmallestNumber:

    def __init__(self):
        self.numbers = []

    def get_number(self):
        while True:
            try:
                number = input("Enter a number: ")
                if number == "done":
                    break
                self.numbers.append(int(number))
            except:
                print ("Invalid input")
            False

    def largest_number(self):
        largest = None
        for number in self.numbers:
            if largest is None:
                largest = number
            elif number > largest:
                largest = number
        return largest

    def smallest_number(self):
        smallest = None
        for number in self.numbers:
            if smallest is None:
                smallest = number
            elif number < smallest:
                smallest = number
        return smallest

    def print_result(self, largest, smallest):
        print("Maximum is ", largest, "Minumum is", smallest)

    def process(self):
        self.get_number();
        largest1 = self.largest_number();
        smallest1 = self.smallest_number();
        self.print_result(largest1, smallest1)


ni = FindLargestAndSmallestNumber()
ni.process()
