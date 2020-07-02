class TimeCalculator:

    def __init__(self):
        self.time_dict = dict()
        #self.global_word_list = list()

    def get_input(self):
        file_name = input("enter file name:")
        global_file = open(file_name)
        return global_file

    def get_times(self, global_file):
        global_word_list=[]
        for line in global_file:
            if line.startswith("From "):
                words = line.split()
                time = words[5]
                hour = time.split(":")
                h = hour[0]
                global_word_list.append(h)
        return global_word_list

    def store_times(self,global_word_list):
        for hour in global_word_list:
            self.time_dict[hour] = self.time_dict.get(hour, 0) + 1
            sorted_time=sorted(self.time_dict.items())
        return sorted_time

    def print_result(self,sorted_time):
        for time,count in sorted_time:
            print(time,count)


    def process(self):
        file=self.get_input();
        time=self.get_times(file);
        print(time)
        time_list=self.store_times(time);
        self.print_result(time_list)

time_list=TimeCalculator()
time_list.process()











