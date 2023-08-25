
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import json
import os

INFLUXDB_URL:str = os.getenv('INFLUXDB_URL')
INFLUXDB_TOKEN:str = os.getenv('INFLUXDB_TOKEN')
INFLUXDB_ORG:str = os.getenv('INFLUXDB_ORG')


jsonlocation = open('artillery-report-data.json','r')


# returns JSON object as
# a dictionary
artilleryReporData = json.load(jsonlocation)
JsonDataInflux = {"measurement": "Artillery Report", "fields": artilleryReporData['aggregate']['counters']}

with InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)

write_api.write(bucket="test_bucket3", record=JsonDataInflux)
client.close()