import json, csv
from collections import OrderedDict
noofTweet = 0
data = []
place = ""
places = {}

with open('output.json') as f:
    for line in f:
        data.append(json.loads(line))

for i in data:
    noofTweet = noofTweet + 1
    if "user" in i.keys():
        place = i['user']['location']
        if place != None:
            place = place.encode('utf-8')
            if place in places.keys():
                places[place] += 1
            else:
                places[place] = 1
    
    if "place" in i.keys():
        if i['place'] != None:
            place = i['place']['full_name']
            place = place.encode('utf-8')
            if place in places.keys():
                places[place] += 1
            else:
                places[place] = 1

places = OrderedDict(sorted(places.items(), key=lambda t: t[1], reverse=True))

writer = csv.writer(open('tags_count.csv', 'wb'))
writer.writerow(["Place_Name", "Tweet_Count"])
for key, value in places.items():
   writer.writerow([key, value])
