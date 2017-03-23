import numpy as np
import random
import tensorflow as tf

class DQN(object):

	def __init__(self, lr, y, e):
		# hyper parameters
		self.lr = lr 	# learning rate
		self.y = y
		self.e = e 		# random action probablity
		self.i = 0
		# These lines establish the feed-forward part of the network
		# used to choose actions
		self.inputs1 = tf.reshape(tf.placeholder(shape=[32,32],dtype=tf.float32), [1,1024])
		self.W = tf.Variable(tf.random_uniform([1024,3],0,0.01))
		self.output = tf.matmul(self.input, self.W)
		self.predict = tf.argmax(self.output, 1)

		# Below we obtain the loss by taking the sum of squares
		# difference between the target and prediction Q values.
		self.nextQ = tf.placeholder(shape=[1,3],dtype=tf.float32)
		self.loss = tf.reduce_sum(tf.square(nextQ - Qout))
		self.trainer = tf.train.GradientDescentOptimizer(learning_rate=self.lr)
		self.updateModel = trainer.minimize(loss)

		# initialize session
		self.init = tf.initialize_all_variables()
		self.sess = tf.Session()

		# action set
		self.actions = [0, 1, 2] # TODO: change to enum

	def start(self):
		"""start a session"""
		self.sess.run(self.init)

	def stop(self):
		"""end a session"""
		self.sess.close()

	def update(self, state, reward):
		""" compute loss and update the network with next state and reward"""

		# obtain the Q' values by feeding the new state through the network
        Q1 = sess.run(self.output,feed_dict={self.input:state})
        max_Q1 = np.max(Q1)
        target_Q = self.Q
        target_Q[0, self.a[0]] = reward + self.y * max_Q1

        # train our network using target and predicted Q values
        self.sess.run([self.updateModel,self.W],
        	feed_dict={self.input:self.current_state,self.target:target_Q})

	def feed_forward(self, state):
		"""feed forward the network with a state to get an action vector"""

		# Choose an action by greedily (with e chance of random action) from the Q-network
        self.a, self.Q = sess.run([self.predict, self.output],
        	feed_dict={self.input:state})
        self.current_state = state

        # e chance to select a random action
        if np.random.rand(1) < e:
        	self.a[0] = self.get_random_action()
			
		self.i += 1
		self.e = 1./((self.i/50.0) + 10)

        return self.a, self.Q

    def get_random_action(self):
    	"""get a random action from actions"""
    	return random.choice(self.actions)