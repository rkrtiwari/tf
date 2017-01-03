import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
c = tf.add(a,b)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

sess.run(c)
print sess.run(c)
sess.close()
