import airodump_csv_to_json
import glob
import csv
import json
import requests
import pprint

airodump_csv_to_json.convert()
print(len(glob.glob1('./',"*kismet.csv")))

with open('dump.json') as data_file:
    data = json.load(data_file)

headers = {'Content-type': 'application/json; charset=utf-8'}
payload = {'status':'OK', 'mobile_signal':data}
r = requests.post('http://localhost:3001/mobile_signal/', data=json.dumps(payload), headers=headers)
print r.status_code
