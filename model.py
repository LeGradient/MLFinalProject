import numpy as np
import math
import data
'''
format as:
[[year, ownership, gender, 1, region0, ..., region_k, r, d1r, ..., d4r], ...]
'''


class Data:
    def __init__(self, data):
        self.x, self.y = self.separate_matrix(data)

    def separate_matrix(self, matrix):
        x = matrix[:, :-5]
        y = matrix[:, -5:]
        return x, y

    def cfs_train(self, l=10e-6):
        ''' closed form solution training '''
        self.w = [calculate_weights(self.x, self.y[:, i], l) for i in range(5)]

    def evaluate(self, year, ownership, gender, region):
        x_new = [year, ownership, gender, 1]+one_hot_regions(region)
        return [np.array(x_new).dot(self.w[i]) for i in range(5)]

    def eval(self):
        return [np.inner(self.w[i], self.x) for i in range(5)]

    def mse(self, data=None):
        if data is None:
            data = self
        return [np.mean((data.y[:, i] - self.eval()[i])**2) for i in range(5)]


def calculate_weights(x, y, l):
    return np.dot(np.linalg.inv(x.T.dot(x)+np.eye(x.shape[1])*l), x.T.dot(y))


def one_hot_regions(region_id):
    return list(map(int, "{0:031b}".format(2**int(region_id))))


stuff = Data(data.matrix)
# print stuff.x.shape, stuff.y[:,0].shape
# print calculate_weights(stuff.x, stuff.y[:,0], 0)
stuff.cfs_train()
print stuff.w[0]
print stuff.w[1]
print stuff.w[2]
print stuff.w[3]
print stuff.w[4]
print "Test Data Point:", stuff.evaluate(2011, 0, 1, 0)
print "MSE: ", stuff.mse()
print "RMSE: ", [math.sqrt(stuff.mse()[i]) for i in range(5)]
