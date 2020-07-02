class Score:
    def __init__(self,number):
        self.number=number

#score = input("Enter Score: ")
#score = float(score)
    def compare_score(self, number):
        if number > 1.0:
            return ("value is out of range")
        elif number >= 0.9:
            return ("A")
        elif number >= 0.8:
            return ("B")
        elif number >= 0.7:
            return ("C")
        elif number >= 0.6:
            return ("D")
        elif number < 0.6:
            return("f")

s1=Score(0.5)
print(s1.compare_score(0.5))


