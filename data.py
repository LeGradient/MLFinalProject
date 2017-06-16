import numpy as np
from scipy import stats

# map region key to integer
def region_index(regions, region):
    return regions.index(region)
# map public/private to bit
def ownership_index(ownership):
    return int(ownership == '"PRIVATE"')
# map gender to bit
def gender_index(gender):
    return int(gender == '"F"')

def one_hot_regions(region_id):
    return list(map(int, "{0:031b}".format(2**int(region_id))))


# generate filenames for 2003.csv - 2016.csv
years = ["ml{}.csv".format(i) for i in range(2003, 2016 + 1)]

# parse the NECTA ID to region & ownership mapping file as a dictionary
with open("master.csv", "r") as infile:
    dictionary = infile.read().split("\n")
dictionary = {item.split(",")[0]: (item.split(",")[1], item.split(",")[2], item.split(",")[3]) for item in dictionary}

# parse the region list
with open("regions.csv", "r") as infile:
    regions = infile.read().split("\n")
regions = [item.split(",")[0] for item in regions][:-1]

# parse each data file
data = []
for i in range(0, len(years)):
    with open(years[i], "r") as infile:
        data.append(infile.read().split("\n"))
    data[i] = [item.split(",") for item in data[i][:-1]]
    for j in range(0, len(data[i])):
        data[i][j][0] = int(data[i][j][0][1:5])
        data[i][j][1] = one_hot_regions(region_index(regions, data[i][j][1]))
        data[i][j][2] = ownership_index(data[i][j][2])
        data[i][j][3] = gender_index(data[i][j][3])
        data[i][j][4] = float(data[i][j][4][1:7])
        data[i][j][5] = float(data[i][j][5][1:7])
        data[i][j][6] = float(data[i][j][6][1:7])
        data[i][j][7] = float(data[i][j][7][1:7])
        data[i][j][8] = float(data[i][j][8][1:7])
        data[i][j].append(1)
        # TODO: unfuck this entire mess
        temp = [data[i][j][0]]
        temp.extend(data[i][j][2:4])
        temp.append(data[i][j][9])
        temp.extend(data[i][j][1])
        temp.extend(data[i][j][4:9])
        data[i][j] = temp

matrix = []
for elt in data[1:]:
    # skip year 2012 because it is an outlier
    if data.index(elt) == 9:
        continue
    matrix.extend(elt)
matrix = np.array(matrix)
matrix[:,0] = stats.zscore(matrix[:,0])
# perm = np.argsort([0,4,1,2,5,6,7,8,9,3])
# matrix = matrix[:,perm]

data2003 = np.array(data[0])
data2016 = np.array(data[-1])

# TODO: drop the name column from years 2003 - 2010 so everything can be indexed the same
# TODO: drop last (empty) column from years 2003 - 2009, 2011, 2016
# TODO: create mapping of region id to list index for one-hot
# TODO: find average pass rate per region per year
#           format as [[year, ownership, gender, 1, isRegion0, isRegion1, ..., isRegion_k, passrate, d1rate, ..., d4rate], ...]
