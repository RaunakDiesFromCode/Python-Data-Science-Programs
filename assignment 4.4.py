import statistics

numbers_list = [1, 2, 3, 4, 5, 5, 6, 7, 8]
mean = statistics.mean(numbers_list)
median = statistics.median(numbers_list)
mode = statistics.mode(numbers_list)
variance = statistics.variance(numbers_list)
stdev = statistics.stdev(numbers_list)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {stdev}")
