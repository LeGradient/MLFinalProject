import numpy as np
import math
import data
'''
format as:
[[year, ownership, gender, region0, ..., region_k, r, d1r, ..., d4r, 1], ...]
'''


class Data:
    def __init__(self, data):
        self.x, self.y = self.separate_matrix(data)

    def separate_matrix(self, matrix):
        x = matrix[:, :-5]
        # Year Feature Multiplication
        print x.shape
        x_new = np.insert(x, 0, x[:, 0]*x[:, 0:34].T, axis=1)
        print x_new.shape
        # Year Sqaured Feature Multiplication
        x_new = np.insert(x_new, 0, (x[:, 0]**2)*x[:, 1:34].T, axis=1)
        #
        # Hadamard product:
        #
        # a1   b11 b12     a1b11 a1b12
        # a2   b21 b22   = a2b21 a2b22
        # a3   b31 b32     a3b31 a3b32
        #
        # Ownership Feature Multiplication
        x_new = np.insert(x_new, 0, x[:, 1]*x[:, 1:34].T, axis=1)

        # Gender Feature Multiplication
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
        x_new = np.insert(x_new, 0, (x[0]**2)*x[1:34])
        x_new = np.insert(x_new, 0, x[1]*x[1:34])
        x_new = np.insert(x_new, 0, x[2]*x[2:34])
        #print x_new.shape
        return [np.array(x_new).dot(self.w[i]) for i in range(5)]

    def eval(self, data=None):
        if data is None:
            data = self
        return [np.inner(self.w[i], data.x) for i in range(5)]

    def mse(self, data=None):
        if data is None:
            data = self
        return [np.mean((data.y[:, i] - self.eval(data)[i])**2) for i in range(5)]


def calculate_weights(x, y, l):
    return np.dot(np.linalg.inv(x.T.dot(x)+np.eye(x.shape[1])*l), x.T.dot(y))


def one_hot_regions(region_id):
    return list(map(int, "{0:031b}".format(2**int(region_id))))


earlyset = Data(data.matrix)

earlyset_test = Data(data.matrix_test)
# print stuff.x.shape, stuff.y[:,0].shape
# print calculate_weights(stuff.x, stuff.y[:,0], 0)
earlyset.cfs_train()


# print "Test Data Point:", earlyset.evaluate(2011, 0, 1, 0)
earlyset_mse = earlyset.mse()
earlyset_test_mse = earlyset.mse(earlyset_test)
print "2003-2011:"
# print "Training MSE: ", earlyset_mse
print "\tTraining RMSE: ", [math.sqrt(earlyset_mse[i]) for i in range(5)]
# print "Test MSE: ", earlyset_test_mse
print "\tTest RMSE: ", [math.sqrt(earlyset_test_mse[i]) for i in range(5)]


lateset = Data(data.matrix2)
lateset_test = Data(data.matrix2_test)
lateset.cfs_train()
lateset_mse = lateset.mse()
lateset_test_mse = lateset.mse(lateset_test)
print "2013-2016:"
# print "MSE:", lateset_mse
print "\tTraining RMSE", [math.sqrt(lateset_mse[i]) for i in range(5)]
# print "Test MSE: ", lateset_test_mse
print "\tTest RMSE: ", [math.sqrt(lateset_test_mse[i]) for i in range(5)]


print "Evalutation Battery: "
# set.evaluate(z-score year, ownership, gender, region id)
print earlyset.evaluate((2006-data.year_mean)/data.year_var, 0, 1, 0)
