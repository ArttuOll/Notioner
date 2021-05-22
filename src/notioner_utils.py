"""Defines functions and procedures required by all Notion integrations."""

import json
from os import path
from sys import stderr, stdin

from dotenv import dotenv_values
import requests

ENV_VARIABLES = dotenv_values(path.join(path.dirname(__file__), "../.env"))
URL = "https://api.notion.com/v1/pages"

def read_json_data_from_stdin():
    """Reads the JSON output of another program into a dict in Notioner. This is how Notioner reads
    data from other programs."""
    json_string = stdin.read()
    return json.loads(json_string)


def read_body_template_json_from_file():
    """Reads the request body template of a Notion page or database, contained in a separate
    file."""
    filepath = path.join(path.dirname(__file__),
                         "../request_body_templates/fina_request_template.json")
    try:
        with open(filepath, "r") as body_template_file:
            body_template_string = body_template_file.read()
            return json.loads(body_template_string)
    except IOError as error:
        print(f"Problem opening body template for reading: {error}", file=stderr)
        return {}


def post_data_to_notion(data):
    """Makes a POST request to Notion, using the standard headers defined by the Notion API."""
    headers = {
                "Authorization": f"Bearer {ENV_VARIABLES['API_KEY']}",
                "Content-Type": "application/json",
                "Notion-Version": "2021-05-13"
              }
    response = requests.post(URL, headers=headers, json=data)
    if response.status_code != 200:
        print(f"Posting data to Notion failed: {response.status_code} - {response.reason}",
              file=stderr)


def get_environment_variables():
    """Returns the contents of the global .env file as dict. This is where API-keys and DB-ids are
    stored in this program."""
    return ENV_VARIABLES
