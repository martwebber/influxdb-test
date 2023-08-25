
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import json


jsonlocation = open('artillery-report-data.json','r')


# returns JSON object as
# a dictionary
artilleryReporData = json.load(jsonlocation)
JsonDataInflux = {"measurement": "Artillery Report", "fields": artilleryReporData['aggregate']['counters']}

with InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_BUCKET, org=INFLUXDB_ORG) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)

write_api.write(bucket=INFLUXDB_BUCKET, record=JsonDataInflux)
client.close()