
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time




def initialize_coing_flips():
    return 2*np.random.randint(2, size=(50,100))-1

def flip_coin():
    return 2*np.random.randint(2)-1

#Global variables are normally a bad idea!!
global num_students
num_students = int(50)
#Mean Squared Displacements

#1D
def msd_1d(x):
    result = np.zeros_like(x)
    for i in range(1,len(x)):
        result[i] = np.average((x[i:] - x[:-i])**2)
    return result

#2D
def msd_2d(x):
    result = np.zeros_like(x)
    for i in range(1, x.shape[1]):
        result[:, i] = np.average((x[:, i:] - x[:, :-i])**2, axis=1)
    return result

def numpy_looping_function():
    num_trials = int(100)
    data_array = np.zeros((50,100,4))
    for n in range(num_students):
        student_array = data_array[n]
        running_sum = 0.0
        for i in range(num_trials):
            student_array[i][0] = int(i+1)
            coin_flip = flip_coin()
            running_sum += coin_flip
            student_array[i][1] = coin_flip
            student_array[i][2] = running_sum
            student_array[i][3] = 0
        student_array[:, 3] = msd_1d(student_array[:, 2])
    meaned_array = np.mean(data_array, axis=0)
    return data_array, meaned_array

def vectorized_function():
    coin_flips_array = initialize_coing_flips()
    med_dist = np.cumsum(coin_flips_array, axis = 1)
    msd_displacement = msd_2d(med_dist)
    data_array = np.dstack((coin_flips_array, med_dist, msd_displacement))
    meaned_array = np.mean(data_array, axis=0)
    return data_array, meaned_array

def plot_creator(data_array, meaned_array, index, y_axis, graph_name, filename):
    colors = plt.cm.jet(np.linspace(0,1,num_students))
    trials = np.arange(0, 100)
    for i in range(num_students):
        plt.plot(data_array[i, :, index],  marker='', color=colors[i])
    plt.plot(meaned_array[:, index], color='purple', linewidth=5)
    plt.legend(handles = [mpatches.Patch(color='purple', label="Ensemble Average")])
    plt.title(graph_name)
    plt.xlabel("Trials")
    plt.ylabel(y_axis)
    plt.savefig(filename)
    plt.show()

def main():
    tic = time.perf_counter()
    data_array, meaned_array = numpy_looping_function()
    toc1 = time.perf_counter()
    vectorized_array, vect_mean = vectorized_function()
    toc2 = time.perf_counter()

    print(f"Looping created arrays in {toc1 - tic:0.4f} seconds")
    print(f"Vectorizing created arrays in {toc2 - toc1:0.4f} seconds")
    plot_creator(data_array=vectorized_array, meaned_array=vect_mean, index = 1, y_axis="Displacements" ,graph_name='Individual Displacements', filename='results/IndividualDisplacements.png')
    plot_creator(data_array=vectorized_array, meaned_array = vect_mean, index = 2,  y_axis="Mean_Squared_Displacement" ,graph_name='Running Average Displacements', filename='results/Running_Average_Displacements.png')


if __name__ == "__main__":
    main()
