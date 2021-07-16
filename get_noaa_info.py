import urllib.request
import json
import os 
from dotenv import load_dotenv

load_dotenv()
offset = 1
number = 0
header = {'token': os.environ['apitoken']}

for i in range(2):
    url = f'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:10003&startdate=2018-01-01&enddate=2018-01-31&limit=1000&offset={offset}'
    request = urllib.request.Request(url ,headers=header)
    with urllib.request.urlopen(request) as f:
        #string = f.read().decode('utf-8')
        object = json.loads(f.read())
        with open (f'data/daily_summaries/daily_summaries_FIPS10003_jan_2018_{number}.json', 'w') as f:
            json.dump(object, f)
    number += 1
    offset += 1000
