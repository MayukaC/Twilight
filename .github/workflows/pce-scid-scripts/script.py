#!/bin/python3
import os
import json

def main():
    base_configurations_list = []
    json_object = {}
    directory = os.getcwd()
    print(directory)
    for path, _, files in os.walk("tenants"):
        for file in files:
            if file.startswith("base-configuration.json"):
                base_configurations_list.append(os.path.join(path, file))
    print(base_configurations_list)

    for scidFilePath in base_configurations_list:
        values = []
        with open(scidFilePath) as f:
            data = json.load(f)
            addresses = data['customer']['addresses']
            for address in addresses:
                if address['type'] == "installation":
                    temp = {}
                    # scidFilePath - 'tenants/HPEGreenLakeCOE-c2cc1mvs57r58ikoq8d0/service-instances/b90f395e-a4af-5a5a-ae1d-f9a08574fb98/scid/base-configuration.json'
                    splitList = scidFilePath.split('/')
                    temp['tenantID'] = splitList[1].split('-')[1]
                    temp['siteID'] = splitList[3]
                    temp['city'] = address['city']
                    temp['state'] = address['state']
                    temp['country'] = address['country']
                    temp['zip'] = address['zip']
                    values.append(temp)
    json_object['config'] = values

    jsonString = json.dumps(json_object)
    jsonFile = open("scidConfig.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

if __name__ == "__main__":
    main()
