#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

highsalary = 0
highsalaryguy = []
for key in data_dict:
    if data_dict[key]["salary"] > 1000000 and data_dict[key]["salary"] != "NaN" and key != "TOTAL":
        highsalary = data_dict[key]["salary"]
        highsalaryguy.append(key)

print highsalary, highsalaryguy

features = ["salary", "bonus"]

for name in data_dict:
        # float() does not include NaN values
    bonus = float(data_dict[name]["bonus"])
    salary = float(data_dict[name]["salary"])
    if bonus >= 5000000 and salary >= 1000000:
        print name, "bonus: ", data_dict[name]["bonus"], "salary: ", data_dict[name]["salary"]


data = featureFormat(data_dict, features)


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
