#Javascript Object notation
import json

# dict = '{"Kunal":"good boy" , "yash":"bad boy"}'
# data = json.loads(dict)
# print(data)
# print(data['Kunal'])


# f = open('data.json') #load function reads json file
# print(f.read())

dict2 = {"hobbies":["swimming","dancing", "singing"],
         "car":"scross",
         "bikes":["pulsar", "discover", 300],
         "summer":False}

jsd = json.dumps(dict2) #convert in js readable format
print(jsd)  #{"hobbies": ["swimming", "dancing", "singing"], "car": "scross", "bikes": ["pulsar", "discover", 300], "summer": false}



