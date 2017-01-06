import tensorflow as tf

## Initial declaration
x = tf.constant(2.0)
y_ = tf.constant(4.0)

w = tf.Variable(1.0)

y = tf.multiply(x, w)

## Loss function creation
loss = tf.square(y - y_)

## Initialization and session setup
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)
print sess.run(loss)

## Optimization

opt = tf.train.GradientDescentOptimizer(learning_rate=0.1)
for i in range(100):
    sess.run(opt.minimize(loss))
    print sess.run(loss), sess.run(w)

#print sess.run(loss)
#print sess.run(w)

sess.close()
