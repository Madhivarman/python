from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

#import required libraries
import numpy as np
import tensorflow as tf
import pandas as pd


TRAINING = 'final_dataset/train_set_data.csv'
TESTING = 'final_dataset/test_set_data.csv'

#to know row and column details in the datasets
TRAINING_SHAPE = pd.read_csv(TRAINING,skiprows=[0],header=None)
TESTING_SHAPE = pd.read_csv(TESTING,skiprows=[0],header=None)

#print("No.of.Rows in the Training_set is:",TRAINING_SHAPE.shape)
#print("No.of.Rows in the Testing_set is:",TESTING_SHAPE.shape)

"""This will output as 
No.of.Rows in the Training_set is: (348978, 50)
No.of.Rows in the Testing_set is: (523466, 49)
"""

#load_datasets
#convert the data into numpy arrays
training_data = TRAINING_SHAPE.as_matrix()
testing_data = np.float32(TESTING_SHAPE.values)


#nodes in the network
n_nodes_h1 = 50
n_nodes_h2 = 50
n_classes = 2
batch_size = 500

x = tf.placeholder('float',[None,50]) #inputs
y = tf.placeholder('float') #labels



def NeuralNetworkModel(data) :


	hidden_1_layer = {'weights':tf.Variable(tf.truncated_normal([50,n_nodes_h1],stddev=0.1)),
					  'biases':tf.Variable(tf.constant(0.1,shape=[n_nodes_h1]))}

	hidden_2_layer = {'weights':tf.Variable(tf.truncated_normal([n_nodes_h1,n_nodes_h2],stddev=0.1)),
					  'biases':tf.Variable(tf.constant(0.1,shape=[n_nodes_h2]))}

	output_layer = {'weights':tf.Variable(tf.truncated_normal([n_nodes_h2,n_classes],stddev=0.1)),
					'biases':tf.Variable(tf.constant(0.1,shape=[n_classes]))}


	#(input_data * weight ) + biases

	layer1 = tf.add(tf.matmul(data,hidden_1_layer['weights']),hidden_1_layer['biases'])
	layer1 = tf.nn.relu(layer1) #activation layer

	layer2 = tf.add(tf.matmul(layer1,hidden_2_layer['weights']), hidden_2_layer['biases'])
	layer2 = tf.nn.relu(layer2)

	output = tf.matmul(layer2,output_layer['weights']) + output_layer['biases']

	return output


#train the model

def TrainNeuralNetwork(x):

	prediction = NeuralNetworkModel(x)
	#cost function
	cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction,labels=y))
	#optimizer
	optimizer = tf.train.AdamOptimizer().minimize(cost)

	#how many epochs ?
	hm_epochs = 100

	#shuffle the dataset order
	training_data  = shuffle(training_data)
	#start the session

	with tf.Session() as sess:
		#run the session
		sess.run(tf.global_variables_initializer())

		for epochs in range(hm_epochs):

			epoch_loss = 0

			#loop over all batches
			for batches in range(int(len(TRAINING_SHAPE) / batch_size)):

				epoch_x = training_data[batches:batch_size,:]
				epoch_y = training_data[batches:batch_size,:]

				_ , c = sess.run([optimizer,cost],feed_dict = {x:epoch_x,y:epoch_y})

				epoch_loss  += c

				print('Epoch:',epochs , 'Completed out of:',hm_epochs , 'loss:',epoch_loss)

		correct = tf.equal(tf.argmax(prediction,1),tf.argmax(y,1))

		accuracy = tf.reduce_mean(tf.cast(correct,'float'))

		print("Accuracy:",accuracy.eval({x:training_data,y:y}))





#function  calling

TrainNeuralNetwork(x)



		

