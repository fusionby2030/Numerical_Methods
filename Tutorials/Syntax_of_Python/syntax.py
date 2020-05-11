#Sample program 3
print("Starting Program")


def create_list(some_input): #2
    sample_list = [] #4ci
    is_20 = False #4d
    for i in range(50): #i: 4bi , range: 4ciii
        if i == 20:
            is_20 = True
            break #1
        sample_list.append(some_input) #1, 4ci
    return sample_list, is_20
sample_string = 'Hello World' #4ai
sample_tuple = create_list(sample_string) #4cii
