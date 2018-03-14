import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

trX = np.linspace(-1,1,101)
trY = 2*trX + np.random.randn(*trX.shape)*0.4+0.2

X = tf.placeholder('float',name='X')
Y = tf.placeholder('float',name='Y')

with tf.name_scope('Model'):
    def model(X,w,b):
        return tf.multiply(X,w)+b
    w = tf.Variable(-1.0,name='w0')
    b = tf.Variable(-2.0,name='b0')
    y_model = model(X,w,b)

with tf.name_scope('CostFunction'):
    cost = (tf.pow(Y-y_model,2))

train_op = tf.train.GradientDescentOptimizer(0.05).minimize(cost)

sess = tf.Session()
init = tf.global_variables_initializer()

tf.train.write_graph(sess.graph,'./','graph.pbtxt')
cost_op = tf.summary.scalar('loss',cost)
merged = tf.summary.merge_all()

sess.run(init)
writer = tf.summary.FileWriter('./',sess.graph)

for i in range(100):
    for (x,y) in zip(trX,trY):
        sess.run(train_op,feed_dict={X:x,Y:y})
        summary_str = sess.run(cost_op,feed_dict={X:x,Y:y})
        writer.add_summary(summary_str,i)
b0temp = b.eval(session=sess)
w0temp = w.eval(session=sess)

plt.plot(trX,b0temp+w0temp*trX)
print(sess.run(w))
print(sess.run(b))
plt.scatter(trX,trY)
plt.plot(trX,0.2+2*trX)
plt.plot(trX,trX*sess.run(w)+sess.run(b))
plt.show()



