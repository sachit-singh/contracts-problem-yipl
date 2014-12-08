import csv
from collections import defaultdict
from operator import itemgetter

from geopy.geocoders import Nominatim

with open('awards.csv') as awards:
    awards_reader = csv.DictReader(awards)
    awards_list = []
    for row in awards_reader:
        awards_list.append(row)

with open('contracts.csv') as contracts:
    contracts_reader = csv.DictReader(contracts)
    contracts_list = []
    for row in contracts_reader:
        contracts_list.append(row)

temp_dict = defaultdict(dict)

for list_item in (contracts_list, awards_list):
    for item in list_item:
        temp_dict[item['contractname']].update(item)

merged = sorted(temp_dict.values(), key=itemgetter('contractname'))

total_closed_awarded_contracts = 0

for row in merged:
    if 'awardee' in row:
        if row['status'] == 'Closed':
            total_closed_awarded_contracts += int(row['Amount'])

result = 'The total amount of closed awarded contracts :' + str(total_closed_awarded_contracts)

geolocator = Nominatim()

list_of_locations = []

for row in merged:
    if 'awardeeLocation' in row:
        location = row['awardeeLocation']
        list_of_locations.append(location)
        location = geolocator.geocode(row['awardeeLocation'])
        print 'loading.....'
        if location is not None:
            row['latlon'] = (location.latitude, location.longitude)

keys = [item for item in merged[1]]

with open('final.csv', 'wb') as output:
    csv_converter = csv.DictWriter(output, keys)
    csv_converter.writer.writerow(keys)
    csv_converter.writerows(merged)

print result