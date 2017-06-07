import numpy as np
import data
'''
format as:
[[year, ownership, gender, 1, isRegion0, isRegion1, ..., isRegion_k, pass, d1rate, ... d4rate], ...]
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
        self.w = np.array([calculate_weights(self.x, self.y[:,i], l) for i in range(5)])

    def evaluate(self, year, ownership, gender, region):
        #x_new = [year, gender] + list(map(int, "{0:031b}".format(2**i))) + [1, 0, 0, 0, 0]
        print one_hot_regions(region)
        #x_news = [[year, ownership, gender, 1]+one_hot_regions(region) + list(map(int,"{0:05b}".format(2**(4-i)))) for i in range(5)]
        x_new = [year, ownership, gender, 1]+one_hot_regions(region)

        print np.array(x_new[0]).dot(np.array(self.w)[:,0])        

def calculate_weights(x, y, l):
    return np.dot(np.linalg.inv(np.dot(x.T,x) + l*np.identity(len(x[0]))), x.T.dot(y)) 
    #return np.dot( np.linalg.inv(x.T.dot(x))  ,x.T.dot(y))
    
def one_hot_regions(region_id):
    return list(map(int, "{0:031b}".format(2**int(region_id))))



stuff = Data(data.matrix)
print stuff.x.shape, stuff.y[:,0].shape
print calculate_weights(stuff.x, stuff.y[:,0], 0)
stuff.cfs_train(0)
#print stuff.w[0]
stuff.evaluate(2016, 1, 1, 13)
