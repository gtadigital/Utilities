
import json
import csv

input_file = open ('JSON/all.json')
json_array = json.load(input_file)
object_list = []

for item in json_array:
    object_details = {"_system_object_id":None,"preview_url":None,"original_download_url":None,"original_url":None}
    object_details['_system_object_id'] = item['objects'][0]['_system_object_id']
    try:
    	object_details['preview_url'] = item['objects'][0]['do']['do_digitalobject'][0]['versions']['preview']['url']
    except:
    	print("non trovato")
    try:
    	object_details['original_download_url'] = item['objects'][0]['do']['do_digitalobject'][0]['versions']['original']['download_url']
    except:
    	print("non trovato")
    try:
    	object_details['original_url'] = item['objects'][0]['do']['do_digitalobject'][0]['versions']['original']['url']
    except:
    	print("non trovato")

    #object_details['type'] = item['type']
    object_list.append(object_details)

print(object_list)

csv_columns = ['_system_object_id','preview_url','original_download_url','original_url']
dict_data = object_list
csv_file = "test.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")
