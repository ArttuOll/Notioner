"""Integrates fina into notion. Reads the fina-notion-template and fills its empty fields with
appropriate data."""

from notioner_utils import read_json_data_from_stdin, read_body_template_json_from_file, post_data_to_notion, get_environment_variables

DATA_TYPE_INDICES_IN_FINA_JSON = {
                                    "income": 0,
                                    "expenses": 1,
                                    "savings": 2
                                  }

def _send_fina_data_to_notion(template, database_id, index_in_fina_data):
    data = template.copy()
    for key, value in json_data[0]["data"][index_in_fina_data]["data"].items():
        data["properties"]["Name"]["title"][0]["text"]["content"] = key
        data["properties"]["Määrä"]["number"] = value

        data["parent"]["database_id"] = database_id
        data["properties"]["Kuukausi"]["select"]["name"] = json_data[0]["month"]
        # post_data_to_notion(data)
        print(data)


json_data = read_json_data_from_stdin()
body_template_json = read_body_template_json_from_file()
environment_variables = get_environment_variables()

_send_fina_data_to_notion(body_template_json,
                          environment_variables["INCOME_DB_ID"],
                          DATA_TYPE_INDICES_IN_FINA_JSON["income"])
_send_fina_data_to_notion(body_template_json,
                          environment_variables["EXPENSES_DB_ID"],
                          DATA_TYPE_INDICES_IN_FINA_JSON["expenses"])
_send_fina_data_to_notion(body_template_json,
                          environment_variables["SAVING_DB_ID"],
                          DATA_TYPE_INDICES_IN_FINA_JSON["savings"])
