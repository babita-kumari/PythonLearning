# Problem_statement: Write a programme to check the given number lies between 0.6 to 1.0.
# Print value is out of range if number is more then 1
# print A if number is greater then equal to 0.9
# print B if number is greater then equal to 0.8
# print C if number is greater then equal to 0.7
# print D if number is greater then equal to 0.6
# print E if number is less then 0.6


class ScoreComparison:

    def get_input(self):
        score=float(0.5)
        return score

    def compare_score(self,score):
        if score > 1.0:
            print ("value is out of range")
        elif score >= 0.9:
            print ("A")
        elif score >= 0.8:
            print ("B")
        elif score >= 0.7:
            print ("C")
        elif score >= 0.6:
            print ("D")
        elif score < 0.6:
            print("E")

    def processes(self):
        score=self.get_input()
        self.compare_score(score)

score_list=ScoreComparison()
score_list.processes()


