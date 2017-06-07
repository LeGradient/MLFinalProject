# get filenames for 2003.csv - 2016.csv
years = ["{}.csv".format(i) for i in range(2003, 2016 + 1)]

# parse the NECTA ID to region & ownership mapping file as a dictionary
with open("master.csv", "r") as infile:
    dictionary = infile.read().split("\n")
dictionary = {item.split(",")[0]: (item.split(",")[1], item.split(",")[2], item.split(",")[3]) for item in dictionary}

# parse each data file
data = []
for i in range(0, len(years)):
    with open(years[i], "r") as infile:
        data.append(infile.read().split("\n"))
    data[i] = [item.split(",") for item in data[i][1:]]

# TODO: drop the name column from years 2003 - 2010 so everything can be indexed the same
# TODO: drop last (empty) column from years 2003 - 2009, 2011, 2016
# TODO: create mapping of region id to list index for one-hot
# TODO: find average pass rate per region per year
#           format as [[year, ownership, isRegion0, isRegion1, ..., isRegion_k, pass rate], ...]

print "sup"


