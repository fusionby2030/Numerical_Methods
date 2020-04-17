import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


np.random.seed(420)

def initialize_coing_flips():
    return 2*np.random.randint(2, size=(50,100))-1
def flip_coin():
    return 2*np.random.randint(2)-1

global num_students
num_students = int(50)


def numpy_function():
    num_trials = int(100)
    data_array = np.zeros((num_students,num_trials,4))
    for n in range(num_students):
        student_array = data_array[n]
        running_sum = 0.0
        running_sum2 = 0.0
        for i in range(num_trials):
            student_array[i][0] = int(i+1)
            coin_flip = flip_coin()
            running_sum += coin_flip
            running_sum2 += (running_sum**2)/(i+1)
            student_array[i][1] = coin_flip
            student_array[i][2] = running_sum
            student_array[i][3] = running_sum2
    #Average for Ensemble
    meaned_array = np.mean(data_array, axis=0)
    return data_array, meaned_array

def vectorized_function():
    #the trial array can be implemented for teh graphs and is not necessary in the arary storage
    data_array = np.zeros((50,100,3))
    coin_flips_array = initialize_coing_flips()
    for i in range(num_students):
        #df = pd.DataFrame(data=data_array[i], columns=['A','B','C','D'])
        student_array = data_array[i]
        student_array[:,0] = coin_flips_array[i]
        #student_array[:,1] = np.cumsum(coin_flip_array[i])
        student_array[:,1] = np.cumsum(student_array[:,0])
        student_array[:,2] = np.cumsum(student_array[:,1])
    meaned_array = np.mean(data_array, axis=0)
    return data_array, meaned_array



def plot_creator(data_array):
    """
    Function to plot the data for a given array.
    To change for the different graphs, one must change the following variables:
    plt.title
    plt.savefig
    df['C']
    plt.ylabel
    And when calling in main be sure to specify which data_array you are graphing
    """
    colors = plt.cm.jet(np.linspace(0,1,num_students))
    for i in range(num_students):
        df = pd.DataFrame(data=data_array[i], columns=['A','B','C','D'])
        plt.plot(df['A'], df['C'],  marker='', color=colors[i])
    plt.title("Individual Displacments")
    plt.xlabel("Trials")
    plt.ylabel("Displacements")
    plt.savefig('EP4/results/IndividualDisplacements.png')
    plt.show()

def main():
    tic = time.perf_counter()
    data_array, meaned_array = numpy_function()

    toc1 = time.perf_counter()
    vectorized_array, vect_mean = vectorized_function()
    toc2 = time.perf_counter()
"""
    print(f"Numpy created arrays in {toc1 - tic:0.4f} seconds")
    print(f"Vector created arrays in {toc2 - tic:0.4f} seconds")
    #plot_creator(data_array)
"""
if __name__ == "__main__":
    main()


"""
for i in range(num_students):
    df = pd.DataFrame(data=data_array[i], columns=['A','B','C','D'])
    plt.plot(df['A'], df['D'],  marker='', color=colors[i])
plt.title("Individual Mean Squared Displacments")
plt.xlabel("Trials")
plt.ylabel("MSD")
plt.show()
for i in range(num_students):
    df = pd.DataFrame(data=meaned_array, columns=['A','B','C','D'])
    plt.plot(df['A'], df['D'],  marker='', color='m')
plt.title("Ensemble Average  Displacments")
plt.xlabel("Trials")
plt.ylabel("Ensemble Average Displacments")
plt.show()
"""
