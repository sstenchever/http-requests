#! /usr/bin/env python3

import os
import requests

# List of all text files to be searched
# Replace './text_files' with your own directory where your text files are
all_items = os.listdir('./text_files')
# Stores information to be included in POSTS
content_dict = {'title': [], 'name': [], 'date': [], 'feedback': []}
# Temp list for preprocessing file contents
temp_list = []
# Stores lines with '\n' removed
cleaned_file_lines = []

# Replace './text_files/' with your own directory
for files in all_items:
    with open('./text_files/'+files, 'r') as fd:
        file_lines = fd.readlines()
        for temp_line in file_lines:
            temp_list.append(temp_line)

for line in temp_list:
    cleaned_file_lines.append(line.rstrip())

# Populate dictionary with values
counter = 0
for clean_line in cleaned_file_lines:
    if counter == 0:
        content_dict['title'].append(clean_line)
        counter += 1
        continue
    elif counter == 1:
        content_dict['name'].append(clean_line)
        counter += 1
        continue
    elif counter == 2:
        content_dict['date'].append(clean_line)
        counter += 1
        continue
    else:
        content_dict['feedback'].append(clean_line)
        counter = 0
        continue

# Temporary dictionary to hold each value for each key in content_dict and
# send those values in separate POST requests
temp_dict = {}

# Iterates through each key value in content_dict and sends them in separate POST requests
for i in range(len(content_dict['title'])):
    for key in content_dict.keys():
        if temp_dict == {}:
            temp_dict = {key: content_dict[key][i]}
        else:
            temp_dict[key] = content_dict[key][i]

    # Send POST request with dictionary as parameter
    # Replace URL with your own URL to send the POST request to
    r = requests.post('http://google.com', data=temp_dict)
    print(r.status_code)