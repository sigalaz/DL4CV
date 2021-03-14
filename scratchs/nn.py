import numpy as np

class NearestNeighbor:
	def __init__(self):
		pass

	def train(self, X, y):
		"""X is N x D where each row is an example. Y is 1-dimension of size N """
		# the nearest neighbour classifier simply remembers all the training data
		self.Xtr = X
		self.ytr = y

	def predict(self, X):
		"""