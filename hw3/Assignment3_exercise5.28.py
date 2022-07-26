import numpy as np
import statistics as stats

# take a list of responses
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

# TASK (a) get unique elements and counts
unique_elements, counts_elements = np.unique(responses, return_counts=True)
print("Frequency of unique values of the array:")
for b in range(len(unique_elements)):
    print('There are', counts_elements[b], ' values of', unique_elements[b])

# TASK (b) statistics
values, counts = np.unique(responses, return_counts=True)
values = list(values)
counts = list(counts)
print("Statistics of response count")
print(f'Min: {values[counts.index(min(counts))]} occurred {min(counts)} time(s)')
print(f'Max: {values[counts.index(max(counts))]} occurred {max(counts)} time(s)')
print(f'Range: {min(counts)}-{max(counts)}')
print(f'Mean: {stats.mean(counts)}')
print(f'Median: {stats.mean(counts)}')
print(f'Mode: {stats.mode(counts)}')
print(f'Variance: {stats.pvariance(counts)}')
print(f'Standard deviation: {stats.pstdev(counts)}')