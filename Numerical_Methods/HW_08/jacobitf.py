import numpy as np


def jacobi(A, b, N=25, x=None):
    """
    Jacobi Iteration for Solving Systems of Equations
    Ax = B
    @params
    A: list or array: L.H.S of equation, matrix to be decomposed
    b: list or array:  R.H.S of equation, end values
    N: int: number of iterations
    x: list or array: initial guesses, default = None
    """
    if x is None:
        x = np.zeros(len(A[0]))

    D = np.diag(A)
    R = A - np.diagflat(D)

    for i in range(N):
        x = (b - np.dot(R, x))/D
    return x

A = np.array([[1.0, 0.0, 0.0, 0.0], [1.0, 4.0, 1.0, 0.0], [0.0, 1.0, 4.0, 1.0], [0.0, 0.0, 0.0, 1.0]], dtype=float)
B = np.array([0, 6, -27, 0], dtype=float)
numpy_iteration = jacobi(A, B)
import tensorflow as tf

A = tf.constant([[10.0, -2.0, -1.0, -1.0], [-2.0, 10.0, -1.0, -1.0], [-1, -1, 10, -2], [-1, -1, -2, 10]], dtype=tf.float32)
B = tf.constant([[3.0], [15.0], [27.0], [-9.0]])
x = tf.Variable(tf.zeros([4, 1]))
A_inv = tf.matrix_inverse(A)
yy = tf.matmul(A_inv, B)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(yy))
    print(numpy_iteration)
