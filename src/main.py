from sys import stdin
from dotenv import dotenv_values
import json

env_variables = dotenv_values(".env")

json_string = stdin.read()
json_data = json.loads(json_string)
print(env_variables)
