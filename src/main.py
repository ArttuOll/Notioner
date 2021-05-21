from sys import stdin, stderr
from os import path
from dotenv import dotenv_values
import json
import requests

ENV_VARIABLES = dotenv_values(".env")
URL = "https://api.notion.com/v1/pages"

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


def _post_data_to_notion(json_data):
    headers = { 
                "Authorization": f"Bearer {ENV_VARIABLES['API_KEY']}" ,
                "Content-Type": "application/json",
                "Notion-Version": "2021-05-13"
              }
    response = requests.post(URL, headers=headers, json=json_data)
    if response.status_code != 200:
        print(f"Posting data to Notion failed: {response.status_code} - {response.reason}", file=stderr)


json_data = _read_json_data_from_stdin()
body_template_json = _read_body_template_json_from_file()

for key, value in json_data[0]["data"][0]["data"].items():
    body_template_json["properties"]["Name"]["title"][0]["text"]["content"] = key
    body_template_json["properties"]["Määrä"]["number"] = value

    body_template_json["parent"]["database_id"] = ENV_VARIABLES["INCOME_DB_ID"]
    body_template_json["properties"]["Kuukausi"]["select"]["name"] = json_data[0]["month"]
    # _post_data_to_notion(body_template_json)
    print(body_template_json)
