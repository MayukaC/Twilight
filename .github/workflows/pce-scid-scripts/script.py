#!/bin/python3
import os
import json

base_configurations_list = []
json_object = {}

base_configuration_file = "base-configuration.json"
infra_layout_file = "infra-layout.json"

# running locally:- /home/mayuka/go/src/github.com/hpe-hcss/Twilight/tenants

def main():
    for path, _, files in os.walk("tenants"):
        for file in files:
            if file.startswith("base-configuration.json"):
                base_configurations_list.append(path)

    values = []

    for scidFilePath in base_configurations_list:
        temp = {}
        with open(scidFilePath + "/" + infra_layout_file) as f:
            data = json.load(f)
            temp['tenantID'] = data['tenantId']
            temp['siteID'] = data['siteId']
        with open(scidFilePath + "/" + base_configuration_file) as f:
            data = json.load(f)
            addresses = data['customer']['addresses']
            for address in addresses:
                if address['type'] == "installation":
                    temp['city'] = address['city']
                    temp['state'] = address['state']
                    temp['country'] = address['country']
                    temp['zip'] = address['zip']
                    values.append(temp)
    json_object['config'] = values

    jsonString = json.dumps(json_object)
    jsonFile = open("scid-infos.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

if __name__ == "__main__":
    main()
