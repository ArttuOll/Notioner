from sys import stdin, stderr
from os import path
from dotenv import dotenv_values
import json

env_variables = dotenv_values(".env")

def _read_json_data_from_stdin():
    json_string = stdin.read()
    return json.loads(json_string)


def _read_body_template_json_from_file():
    filepath = path.join(path.dirname(__file__), "../request_body_templates/fina_request_template.json")
    try:
        with open(filepath, "r") as body_template_file:
            body_template_string = body_template_file.read()
            return json.loads(body_template_string)
    except IOError as error:
        print(f"Problem opening body template for reading: {error}", file=stderr)



json_data = _read_json_data_from_stdin()
body_template_json = _read_body_template_json_from_file()
