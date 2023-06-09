import json
import os
from pathlib import Path
 
initial = {
    "Format": "1.29.0",
    "ConfigSchema": {},
    "Changes": []
}

json_initial = json.dumps(initial, indent=4)

with open("content.json", "w") as outfile:
    outfile.write(json_initial)

characters_list = []
portraits_list = []
with os.scandir("[CP] Sex Change Mod\\assets\\Characters") as it:
    print("first")

    for cn in it:
        characters_list.append(Path(cn).stem)
    with os.scandir("[CP] Sex Change Mod\\assets\\Portraits") as jt:
        for pn in jt:
            portraits_list.append(Path(pn).stem)

with open('content.json', 'r') as readfile:
    json_object = json.load(readfile)

with os.scandir("[CP] Sex Change Mod\\assets\\Characters") as it:
    print("second")
    for entry in it:
        print("third")
        name = Path(entry).stem
        print(name)
        
        if name in characters_list and name in portraits_list:
            print("fourth")
            json_object['ConfigSchema'][f'Enable {name} portraits'] = {
                "AllowValues": "True, False",
                "Default": "True",                 
            }
            json_object['Changes'].append({
                "Action": "EditImage",
                "Target": f'Portraits/{name}',
                "FromFile": f'assets/Portraits/{name}.png',
                "When": {
                    f'Enable {name} portraits': "True"
                }		          
            })
        json_object['Changes'].append({
            "Action": "EditImage",
            "Target": f'Characters/{name}',
            "FromFile": f'assets/Characters/{name}.png',
            "When": {
                f'Enable {name} sprites': "True"
            }		          
        })
        json_object['ConfigSchema'][f'Enable {name} sprites'] = {
            "AllowValues": "True, False",
            "Default": "True",                 
        }
with open('content.json', 'w') as rwfile:
    rwfile.write(json.dumps(json_object, indent=4))