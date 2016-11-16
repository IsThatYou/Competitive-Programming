import math
from datetime import datetime

loc = input().split(',')
latitude = float(loc[0])
longtitude = float(loc[1])

r = float(input())
R = 6378.137
headers = input().split(',')
TIME = -1
LAT = -1
LON = -1
PHONE = -1


def distance(profile):
    lat2 = float(profile[LAT])
    lon2 = float(profile[LON])
    d = 2 * R * math.asin(
        math.sqrt(math.sin(math.radians((latitude - lat2) / 2)) ** 2) + math.cos(math.radians(latitude)) * math.cos(
            math.radians(lat2)) * (math.sin(math.radians((longtitude - lon2) / 2)) ** 2))
    return d


def transform_t(time):
    date_object = datetime.strptime(time, '%m/%d/%Y %H:%M')
    return date_object


for j in range(4):
    if headers[j].startswith('Date'):
        TIME = j
    elif headers[j].startswith('Lat'):
        LAT = j
    elif headers[j].startswith('Lon'):
        LON = j
    else:
        PHONE = j
phonebook = {}

while True:
    try:
        profile = input()
    except EOFError:
        break

    profile = profile.split(',')
    ptime = profile[TIME]
    dis = distance(profile)
    phone = profile[PHONE]
    if phone in phonebook.keys():
        try:
            time1 = phonebook[phone]
            new = transform_t(ptime)
            old = transform_t(time1)
        except:
            pass
        if new > old:
            if dis > r:
                del phonebook[phone]
            elif dis < r:
                phonebook[phone] = profile[TIME]

    else:
        if dis < r:
            phonebook[phone] = profile[TIME]

a = []
for i in sorted(phonebook.keys()):
    a.append(i)
print(','.join(a))





