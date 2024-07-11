import os
from dotenv import load_dotenv

from influxdb_client_3 import InfluxDBClient3, Point
import requests

load_dotenv()

# Influx DB Credentials
INFLUX_CLUSTER_URL = os.getenv("INFLUX_CLUSTER_URL", "")
INFLUX_ORGANIZATION_ID = os.getenv("INFLUX_ORGANIZATION_ID", "")
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN", "")
INFLUX_BUCKET = os.getenv("INFLUX_BUCKET", "")

# Zenodo Credentials
ZENODO_TOKEN = os.getenv("ZENODO_TOKEN")

# General information
filename = "export.csv"
path = "./data/%s" % filename

# FETCH DATA

INFLUX_QUERY = "SELECT * FROM \"soil\" WHERE time >= now() - interval '1 hour'" # get data for the past hour
client = InfluxDBClient3(token=INFLUX_TOKEN,
                         host=INFLUX_CLUSTER_URL,
                         org=INFLUX_ORGANIZATION_ID,
                         database=INFLUX_BUCKET)
reader = client.query(query=INFLUX_QUERY, language="sql")
reader.to_pandas().to_csv(path) # store file locally

# UPLOAD DATA

headers = {"Content-Type": "application/json"}
params = {'access_token': ZENODO_TOKEN}

# generate a upload URL
r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions',
                   params=params,
                   json={},
                   headers=headers)
bucket_url = r.json()["links"]["bucket"]

# upload file
with open(path, "rb") as fp:
    r = requests.put(
        "%s/%s" % (bucket_url, filename),
        data=fp,
        params=params,
    )
print(r.json())