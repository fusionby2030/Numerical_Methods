import numpy as np
import torch
import matplotlib.pyplot as plt

"""
# tensors look like this

x = torch.tensor(3.)
w = torch.tensor(4., requires_grad=True)
b = torch.tensor(4., requires_grad=True)

# Doing arithmetic

y = w * x + b
# Output
# tensor(17., grad_fn=<AddBackward0>)

# We can then compute the gradients w.r.t to the tensors in y
y.backward()

# Gradients

w_grad = w.grad
# 3
b_grad = b.grad
# 1
""" # Tensor Notation
"""
General Problem: 
Predict target variables using input features 

Linear Regression, each target variable is estimated to be a weighted
 sum of the input variables, offset by some constant (bias)

The objective is to find a suitable set of weights and biases using the training data to make accurate predictions

Sample Problem
Taylor Expansion of a model equation for current 
Inputs: Voltages 
Ouputs: Current 
Determine constants beta and I_S

"""

beta = 5.489
sat_current = 1.87324


def model_eq(v, beta=beta, sat_current=sat_current):
    return sat_current*np.exp(beta*v)


voltages = np.linspace(0, 0.5, num=500, dtype='float32')
currents = np.array(model_eq(voltages), dtype='float32')





# Training Data

# Inputs (temp, rainfall, humidity)
inputs = np.array([[1, x, x**2, x**3, x**4, x**5] for x in voltages], dtype='float32')
# Targets (apples, oranges)
targets = np.array([[x] for x in currents], dtype='float32')
print('Input Shape: {}'.format(inputs.shape))
# print(inputs)
print('Targets Shape: {}'.format(targets.shape))
# print(targets)


def model_fit(input, beta=beta, sat_current=sat_current):
    x0, x1, x2, x3, x4, x5 = input
    return x0*sat_current + x1*beta*sat_current + sat_current*x2*beta**2 + sat_current*x3*beta**3 + sat_current*x4*beta**4 + sat_current*x5*beta**5

current_fit = []
for input in inputs:
    current_fit.append(model_fit(input))


plt.scatter(voltages, currents, label='Data')
plt.plot(voltages, current_fit, label='fit', color='orange')
plt.legend()
plt.show()



# Convert to Tensors

inputs, targets = torch.from_numpy(inputs), torch.from_numpy(targets)

"""
Simple Linear Regression Model Implementation 
"""

# Weights and Biases are tensors initialized with random values.
# This part I am concerned with philosophically, i.e., different random initialized states change output entirely
w = torch.randn(5, 1, requires_grad=True)
b = torch.randn(1, requires_grad=True)


# first row of w and first element of b are used to predict first target variable (apples)
# second row of w and second element of b for second target variable (oranges)

# Matrix multiplication of input x with w transposed plus the bias

def model(x):
    return x @ w.t() + b


# predictions made by passing the input data through model
# preds = model(inputs)

# now we could compare the preds with the targets, but we know it will be quite different

"""
Loss Function 

Used to compare predictions with actual targets
Use Mean Squared Error for comparison 

Loss provides an indication on how bad the model is predicting the target variables. 
Generally a lower loss the better the model ( although many factors play into this )

From calculus we know that the gradient of the loss represents the rate of change of the loss. 
If the gradient of the loss w.r.t element (weight or bias) is:
    positive: 
        increasing the element will increase the loss 
        decreasing the element will decrease the loss
    negative:
        increasing the element will decrease the loss 
        decreasing the element will increase the loss 

"""

from torch.utils.data import TensorDataset, DataLoader
# This will be able to split the data into batches while training, and utilize shuffling and sampling

train_ds = TensorDataset(inputs, targets)

# Define data loader
batch_size = 5
train_dl = DataLoader(train_ds, batch_size, shuffle=True)

# Define Model
model = torch.nn.Linear(5, 1)
# model.weight is equiv. to w
# model.bias is equiv. to b

# Instead of using gradients manual use Stochastic Gradient Descent from optim.SGD

# Define Optimizer
opt = torch.optim.SGD(model.parameters(), lr=1e-5)

# Loss Function is pre build
import torch.nn.functional as F

# Define Loss Function

loss_fn = F.mse_loss

loss = loss_fn(model(inputs), targets)

# Define a utility function to train the model
def fit(num_epochs, model, loss_fn, opt):
    for epoch in range(num_epochs):
        for xb,yb in train_dl:
            # Generate predictions
            pred = model(xb)
            loss = loss_fn(pred, yb)
            # Perform gradient descent
            loss.backward()
            opt.step()
            opt.zero_grad()
    print('Training loss: ', loss_fn(model(inputs), targets))
    print(xb)
    print(pred)
    preds = []
    for volt in inputs:
        preds.append(model(volt))
    return preds


# Train the model for 100 epochs
preds = fit(1000, model, loss_fn, opt)
plt.scatter(voltages, currents, label='Data')
plt.plot(voltages, preds, label='Fit')
plt.legend()
plt.show()