import numpy as np
import data
'''
format as:
[[year, ownership, gender, isRegion0, isRegion1, ..., isRegion_k, pass, d1rate, ... d4rate], ...]
'''


class Data:
    def __init__(self, data):
        self.x, self.y = self.separate_matrix(data)
        

    def separate_matrix(self, matrix):
        x = matrix[:,:-5]
        y = matrix[:,-5:]
        return x, y

    def cfs_train(self, l=0):
        ''' closed form solution training '''
        self.w = [calculate_weights(self.x, self.y[i], l) for i in range(5)]

    def evaluate(self, year, ownership, region, gender):
        #x_new = [year, gender] + list(map(int, "{0:031b}".format(2**i))) + [1, 0, 0, 0, 0]
        x_news = [[year, ownership, gender]+list(map(int, "{0:031b}".format(2**region))) + list(map(int,"{0:05b}".format(2**(i)))) for i in range(5)]
        print x_news
        

def calculate_weights(x, y, l):
    return np.dot(np.linalg.inv(np.dot(x.T,x) + l*np.identity(len(x[0]))), x.T.dot(y)) 

def one_hot_regions(region_id):
    return 

