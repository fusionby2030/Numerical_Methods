import tensorflow as tf
"""Dot product of two 1D matricies """
t1 = tf.constant([4., 3., 2.])

t2 = tf.constant([3., 2., 1.])

dot = tf.tensordot(t1, t2, 1)

# 4*3 + 3*2 + 2*1 = 20
""" Matrix Multiplication of two 2D matricies"""
t3 = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

t4 = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

matmu = tf.matmul(t3, t4)

# [[ 22. 28.], [ 49. 64.]]
""" Einstein Summation """
m1 = tf.constant([[1, 2], [3, 4]])

m2 = tf.constant([[5, 6], [7, 8]])
""" Indicies ijk  outputs are then denoted by the arrow """
e1 = tf.einsum('ij->ji', m1)     # [[1, 3], [2, 4]]
"""compute the element-wise product of tensors t1 and t2"""
e2 = tf.einsum('ij,jk->ik', m1, m2) # [[19, 22], [43, 50]]
with tf.Session() as sess:
    print(dot.eval())
    print(matmu.eval())
    print(e1.eval())
    print(e2.eval())
