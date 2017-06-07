import numpy as np

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
        self.w = calculate_weights(self.x, self.y, l)

    def evaluate(self, year, ownership, region, gender):
        x_new = [year, gender] + [''' 1HOT region'''] + [1, 0, 0, 0, 0]
        x_news = [ [year, gender] + [''' 1HOT1'''] + list(map(int,"{0:05b}".format(2**(4-i)))) for i in range(5) ]
        print x_news
        

def calculate_weights(x, y, l):
    return np.dot(np.linalg.inv(np.dot(x.T,x) + l*np.identity(len(x[0]))), x.T.dot(y)) 


test = np.random.rand(40,30)
testdata = Data(test)
print testdata.x
print testdata.evaluate()
