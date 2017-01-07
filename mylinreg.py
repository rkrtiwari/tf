import tensorflow as tf

#x = tf.random_normal([10], dtype = tf.float32, seed = 100)
# problem with calculation with random number will be looked at a later stage

x = tf.linspace(10.0, 15.0, 10) 

m = tf.constant(5.0)
y = tf.mul(x,m) 

w = tf.Variable(2.5)
y_ = tf.mul(x,w)

loss = tf.reduce_mean(tf.square(y - y_))

opt = tf.train.GradientDescentOptimizer(learning_rate = 0.001)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

for i in range(100):
    sess.run(opt.minimize(loss))
    print  sess.run(w)

print "Final Value"
print sess.run(w)
sess.close()

