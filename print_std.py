import statistics

sum = 0
n = 100
sample=range(1,101)
print(sample)
for i in range(1, n):
    sum += i
print(sum)

average = sum / n
print(average)
print("Standard Deviation of the sample is % s "
                    %(statistics.stdev(sample)))