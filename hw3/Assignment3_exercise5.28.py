import numpy as np
import statistics

# take a list of responses
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

# TASK (a) get unique elements and counts
unique_elements, counts_elements = np.unique(responses, return_counts=True)
print("Frequency of unique values of the array:")
for i in range(len(unique_elements)):
    print('There are', counts_elements[i], ' values of', unique_elements[i])

# TASK (b) statistics
print('\n\nThe Statistics are:')
print('Minimum:', min(responses))
print('Maximum:', max(responses))
print('Range:', max(responses) - min(responses))
print('Median:', statistics.median(responses))
print('Mode:', statistics.mode(responses))
print('Variance:', statistics.variance(responses))
print('Standard Deviation:', statistics.stdev(responses))
