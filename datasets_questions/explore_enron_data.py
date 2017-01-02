#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print("How many people:", len(enron_data))

print("How many features per person:", len(enron_data["METTS MARK"]))
a = enron_data["METTS MARK"]

#person of interest
count_poi = 0
POI = []
for key in enron_data:
    if (enron_data[key]["poi"]) == True:
        count_poi = count_poi + 1
        #print(key)
        POI.append(key)
print count_poi
print POI
print type(POI)
print "___________"

#count number of POIs in text final_project
poi_names = open("../final_project/poi_names.txt").read().split('\n')
poi_y = [name for name in poi_names if "(y)" in name]
print("poi_names_count:", len(poi_y))

print "___________"

#stock value of James Prentice
print ("Total Stock Value of James Prentice", enron_data["PRENTICE JAMES"]["total_stock_value"])

#'Messages from Wesley Cowell to POIs'
print 'Messages from Wesley Cowell to POIs', enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

enron_data["SKILLING JEFFREY K"]
print "___________"

#largest payments brought home
max_total_payments = 0
person_with_mtp = "nobody"
del enron_data["TOTAL"]
for k in enron_data:
    #print k
    if max_total_payments < enron_data[k]["total_payments"] and enron_data[k]["total_payments"] != "NaN" and enron_data[k] != "TOTAL":
        max_total_payments = enron_data[k]["total_payments"]
        person_with_mtp = k

print "Person with largest payment brought home named:",person_with_mtp,"has max_total_payments of", max_total_payments

print "___________"

#how many person have a quantified salary

email_count = 0
for k in enron_data:
    if enron_data[k]['email_address'] != 'NaN':
        email_count += 1
print "number of emails known:", email_count

salary_count = 0
for person in enron_data:
    if enron_data[person]['salary'] != 'NaN':
        salary_count += 1
print "number of salary known:", salary_count
