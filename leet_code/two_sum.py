"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

solution:
step 1: get number list in input and decide target
step 2: calculate the sum of all possible combination of element without repeating the element
step 3: if sum of two elements is equal to target then break the processes
step 4: then return the index value of these two elements
"""


class TwoSum:

    solution_target = 19

    def get_input(self):
        given_number = [4, 5, 7, 8, 9, 10, 12, 45]
        return given_number

    def calculate_sum(self, given_number):
        solution_list=[]
        i = 0
        j = 0
        for i in given_number:
            print("I= ", i)
            for j in given_number:
                print("J=", j)
                sum = i + j
                print("SUM=", sum)
                if sum==self.solution_target:
                    print("found target", i,j)
                    index_i=given_number.index(i)
                    index_j=given_number.index(j)
                    solution_tuple=(index_i,index_j)
                    reverse_solution_tuple=(index_j,index_i)
                    if reverse_solution_tuple in solution_list:continue
                    else:
                        solution_list.append(solution_tuple)
        print(solution_list)
        return solution_list

    def processes(self):
        input = self.get_input();
        print("Input: ", input)
        sum = self.calculate_sum(input)


indices = TwoSum()
indices.processes()
