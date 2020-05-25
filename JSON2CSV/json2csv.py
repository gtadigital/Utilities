'''
author: ETH Zurich, gta digital, Matteo Lorenzini
license: please refer to the license.txt file in our git repository (https://github.com/gtadigital/GeoWrapper)
'''

from os import listdir
from os.path import isfile, join
import json
import csv

dir_path = "JSON/"

#input_file = open ('JSON/test.json')
#json_array = json.load(input_file)
object_list = []

all_json_files = [join(dir_path, f) for f in listdir(dir_path) if isfile(join(dir_path, f)) and f.endswith(".json")]

for file_path in all_json_files:
    with open(file_path) as input_file:
        json_array = json.load(input_file)
        for obj in json_array:
                for item in obj['objects']:
                    object_details = {"_system_object_id":None,"preview_url":None,"original_download_url":None,"original_url":None}
                    object_details['_system_object_id'] = item['_system_object_id']
                    try:
                    	object_details['preview_url'] = item['do']['do_digitalobject'][0]['versions']['preview']['url']
                    except:
                    	object_details['preview_url'] = ('Missing Value')
                    try:
                    	object_details['original_download_url'] = item['do']['do_digitalobject'][0]['versions']['original']['download_url']
                    except:
                    	object_details['original_download_url'] = ('Missing Value')
                    try:
                    	object_details['original_url'] = item['do']['do_digitalobject'][0]['versions']['original']['url']
                    except:
                    	object_details['original_url'] = ('Missing Value')

                    #object_details['type'] = item['type']
                    object_list.append(object_details)
                print(object_list)

csv_columns = ['_system_object_id','preview_url','original_download_url','original_url']
dict_data = object_list
csv_file = "CSV/export.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")
