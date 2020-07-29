import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'
gold = '#ebdb34'
blue = '#34c3eb'
def relu_activation(z):
    return np.maximum(0, z)
def relu_derivative(z):
    dZ = z
    dZ[z <=0] = 0
    return dZ
class NeuralNet():
    def __init__(self, x, y):
        np.random.seed(42)
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 2)
        self.weights2 = np.random.rand(self.input.shape[1], 1)
        self.y = y
        self.output = np.zeros(y.shape)
        self.b = 0.3*np.ones_like(self.input)
        self.c = np.zeros_like(self.output)

    def feedforward(self):
        self.layer1 = relu_activation(np.dot(self.input, self.weights1) + self.b)
        self.output = np.dot(self.layer1, self.weights2) + self.c
        return self.output
    def backprop(self):
        d_weights1 = np.dot(self.layer1.T, (2*self.y - self.output)*relu_derivative(self.output))
        d_weights2 = np.dot(self.input.T, (np.dot(2*(self.y - self.output)*relu_derivative(self.output), self.weights2.T)*relu_derivative(self.layer1)))
        self.weights1 += d_weights1
        self.weights2 += d_weights2
    def train(self, x, y):
        self.output = self.feedforward()
        self.backprop()
0.3*np.ones_like(inxor)
inxor = np.array([[0,0], [0,1], [1,0], [1,1]])
relu_activation(np.dot(inxor, weights1)) - 0.3*np.ones_like(inxor)
outxor = np.array([[0],[1],[1],[0]])
inputs = np.array([[0, 500], [500, 1000], [1000, 2000], [2000, 3000], [3000, 4000]])
outputs = np.array([6000, 4250, 3600, 1500, 650])
weights1 = -1*np.random.rand(inxor.shape[1], 2)
stop = np.dot(inxor, weights1) + 0.2
relu_activation(stop)
inxor.shape
NN = NeuralNet(inxor, outxor)
for i in range(5):
    if i:
        print("iteration {}".format(i))
        print("Input : \n" + str(inxor))
        print('Actual: \n' + str(outxor))
        print("Predicted: \n" + str(NN.feedforward))
        print("Loss: \n" + str(np.mean(np.squar(outxor - NN.feedforward()))))
    NN.train(inxor, outxor)
a = np.array([[1, 2], [2, 2], [3,3]])
a.shape
np.maximum(0, a)
inputs[:, 0]
plt.scatter(inputs[:, 0], outputs)
plt.scatter(inputs[:, 1], outputs)
