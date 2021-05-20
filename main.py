from sys import stdin
import json

json_string = stdin.read()
json_data = json.loads(json_string)
print("Tämä data tulee täältä!!!", json_data)
