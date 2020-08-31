"""
Get the Smallest Number of a List
"""

def find_smallest_number(samples):
    """
    A function to Get the Smallest Number of a List
    arguments
        samples: (list)

    returns smallest number (float or int) of list
    """
    minimum = samples[0]
    for num in samples:
        if num <= minimum:
            minimum = num
            continue
        else:
            pass
    return minimum

expected = 0.1
output = find_smallest_number([0.2, 1.3, 1.6, 0.23, 0.1])

print(output)
