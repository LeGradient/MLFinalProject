with open("master.csv", "r") as infile:
    dictionary = infile.read().split("\n")
dictionary = {item.split(",")[0]: (item.split(",")[1], item.split(",")[2], item.split(",")[3]) for item in dictionary}

with open("2003.csv", "r") as infile:
    data = infile.read().split("\n")
data = [item.split(",") for item in data[1:]]
print data[:10]

