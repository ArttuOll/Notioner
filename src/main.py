from sys import stdin, stderr
from os import path
from dotenv import dotenv_values
import json

env_variables = dotenv_values(".env")

json_string = stdin.read()
json_data = json.loads(json_string)

filepath = path.join(path.dirname(__file__), "../request_body_templates/fina_request_template.json")
try:
    with open(filepath, "r") as body_template_file:
        body_template_string = body_template_file.read()
        body_template = json.loads(body_template_string)
        print(body_template)
except IOError as error:
    print(f"Problem opening body template for reading: {error}", file=stderr)
