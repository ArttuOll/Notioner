import json
from os import path
from sys import stderr, stdin

from dotenv import dotenv_values
import requests

ENV_VARIABLES = dotenv_values(".env")
URL = "https://api.notion.com/v1/pages"
DATA_TYPE_INDICES_IN_FINA_JSON = {
                                    "income": 0,
                                    "expenses": 1,
                                    "savings": 2
                                  }

def _read_json_data_from_stdin():
    json_string = stdin.read()
    return json.loads(json_string)


def _read_body_template_json_from_file():
    filepath = path.join(path.dirname(__file__),
                         "../request_body_templates/fina_request_template.json")
    try:
        with open(filepath, "r") as body_template_file:
            body_template_string = body_template_file.read()
            return json.loads(body_template_string)
    except IOError as error:
        print(f"Problem opening body template for reading: {error}", file=stderr)
        return {}


def _post_data_to_notion(data):
    headers = {
                "Authorization": f"Bearer {ENV_VARIABLES['API_KEY']}",
                "Content-Type": "application/json",
                "Notion-Version": "2021-05-13"
              }
    response = requests.post(URL, headers=headers, json=data)
    if response.status_code != 200:
        print(f"Posting data to Notion failed: {response.status_code} - {response.reason}",
              file=stderr)


def _send_fina_data_to_notion(template, database_id, index_in_fina_data):
    data = template.copy()
    for key, value in json_data[0]["data"][index_in_fina_data]["data"].items():
        data["properties"]["Name"]["title"][0]["text"]["content"] = key
        data["properties"]["Määrä"]["number"] = value

        data["parent"]["database_id"] = database_id
        data["properties"]["Kuukausi"]["select"]["name"] = json_data[0]["month"]
        _post_data_to_notion(data)
        print(data)


json_data = _read_json_data_from_stdin()
body_template_json = _read_body_template_json_from_file()
_send_fina_data_to_notion(body_template_json,
                          ENV_VARIABLES["INCOME_DB_ID"],
                          DATA_TYPE_INDICES_IN_FINA_JSON["income"])
_send_fina_data_to_notion(body_template_json,
                          ENV_VARIABLES["EXPENSES_DB_ID"],
                          DATA_TYPE_INDICES_IN_FINA_JSON["expenses"])
_send_fina_data_to_notion(body_template_json,
                          ENV_VARIABLES["SAVING_DB_ID"],
                          DATA_TYPE_INDICES_IN_FINA_JSON["savings"])
