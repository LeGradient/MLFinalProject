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
        print x.shape
        x_new = np.insert(x, 0, x[:, 0]*x[:, 0:34].T, axis=1)
        #
        # Hadamard product:
        #
        # a1   b11 b12     a1b11 a1b12
        # a2   b21 b22   = a2b21 a2b22
        # a3   b31 b32     a3b31 a3b32
        #
        x_new = np.insert(x_new, 0, x[:, 1]*x[:, 1:34].T, axis=1)
        x_new = np.insert(x_new, 0, x[:, 2]*x[:, 2:34].T, axis=1)
        y = matrix[:, -5:]
        return x_new, y

    def cfs_train(self, l=10e-6):
        ''' closed form solution training '''
        self.w = [calculate_weights(self.x, self.y[:, i], l) for i in range(5)]

    def evaluate(self, year, ownership, gender, region):
        x = np.array([year, ownership, gender, 1]+one_hot_regions(region))
        # print x.shape
        x_new = np.insert(x, 0, x[0]*x[0:34])
        x_new = np.insert(x_new, 0, x[1]*x[1:34])
        x_new = np.insert(x_new, 0, x[2]*x[2:34])
        print x_new.shape
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


earlyset = Data(data.matrix)
# print stuff.x.shape, stuff.y[:,0].shape
# print calculate_weights(stuff.x, stuff.y[:,0], 0)
earlyset.cfs_train()
#print "Test Data Point:", earlyset.evaluate(2011, 0, 1, 0)
earlyset_mse = earlyset.mse()
print "2003-2011:"
print "MSE: ", earlyset_mse
print "RMSE: ", [math.sqrt(earlyset_mse[i]) for i in range(5)]

print data.matrix.shape
lateset = Data(data.matrix2)
lateset.cfs_train()
lateset_mse = lateset.mse()
print "2013-2016:"
print "MSE:", lateset_mse
print "RMSE", [math.sqrt(lateset_mse[i]) for i in range(5)]
