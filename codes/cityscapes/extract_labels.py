#!/usr/bin/python

import json
import csv
import os


json_dir_path = open('/home/san/Dev/dataset/cityscapes/gtFine_trainvaltest/gtFine/train/')

city_list = {'aachen',
             'bochum',
             'bremen',
             'cologne',
             'darmstadt',
             'dusseldorf',
             'erfurt',
             'hamburg',
             'hanover',
             'jena',
             'krefeld',
             'monchenglabach',
             'strasbourg',
             'stuttgart',
             'tubingen',
             'ulm',
             'weimar',
             'zurich'}

# Construct a dictionary
class_dict = {}

# initialze current_index
latest_class_label = 0 #Only add one when it is a new class

# List of category that need to be ignorded
list_of_category_to_ignore = ['unlabeled',
                              'rectification boarder',
                              'out of roi',
                              'static',
                              'dynamic',
                              'ground',
                              "road",
                              'guard rail',
                              'vegetation',
                              "sky"
                              ]


for city in city_list:
    json_city_path = json_dir_path + city
    print("city_path: {}".format(json_city_path))

    for file in os.listdir(json_city_path):
        if file.endswith('.json'):
            # json_file_name = os.path.splitext(image)[0]
            json_file_name_array = file.split("_")
            label_file_path = json_file_name_array[0] + "_" + json_file_name_array[1] + "_" + json_file_name_array[2] + '.txt'

            f = open(label_file_path, "w+")


            print("----- LOADING JSON -----")
            json_data = open(file)
            data = json.load(json_data)

            imgHeight = data['imgHeight']
            imgWidth = data["imgWidth"]

            object_list = data['objects']
            num_of_object = len(object_list)

            for i in range(num_of_object):
                print("[STEP 1] =============  Object number i: ", i)
                object_dict = object_list[i] # The i-th object
                object_polygon = object_dict['polygon']
                object_label = object_dict['label']
                print("current_object_label: {}".format(object_label))

                if object_label in list_of_category_to_ignore:
                    print("The current object label is in the ignore list")
                else:
                    # Check if the label is already in the dictionary
                    if class_dict.has_key(object_label):
                        print("current_object_label is already in the class_dict")
                        # show current size of class_dict
                        print("len(class_dict):  ", len(class_dict))
                    else:
                        print("New Class: add to class_dict")
                        print("label_to_be_added: ", object_label)
                        class_dict[object_label] = latest_class_label
                        # Update label count
                        latest_class_label = latest_class_label + 1
                        # show current size of class_dict
                        print("len(class_dict):  ", len(class_dict))

                # Get X-Y from polygon
                min_x, min_y = 0,0
                for j in range(len(object_polygon)):
                    current_vertice = object_polygon[j]
                    current_vertice_x = current_vertice[0]
                    current_vertice_y = current_vertice[1]

                    if 








            f.close()



print(" --- END OF CLASS DICT CONSTRUCT ---")
print(class_dict.items())

# Save class dictionary to text file
f = open("class_dict.txt","w")
f.write( str(class_dict) )
f.close()

# Save class dictionary to csv file
w = csv.writer(open("class_dict.csv", "w"))
for key, val in class_dict.items():
    w.writerow([key, val])
