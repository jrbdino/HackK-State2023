import taipy as tp
from taipy import Config, Core, Gui
from taipy.gui import Markdown, notify
import pandas as pd
from prioritize import prioritize


def build_message(name):
    return f"Hello {name}!"


def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit()
    state.message = scenario.message.read()


def submit_homework(state):
    state.scenario.csv_node.write(state.csv_node)


def load_csv_file(state):
    local_data = pd.read_csv(state.path)
    data["Assignment"] = local_data.iloc[:, 0]
    data['Weight'] = local_data.iloc[:, -1]
    state.data = data

def edit_df(state, varname, payload):
    index = payload["index"]
    col = payload["col"]
    value = payload["value"]
    user_value = payload["user_value"]

    old_value = state.local_data.loc[index, col]
    new_df = state.local_data.copy()
    new_df.loc[index, col] = value
    state.local_data = new_df
    notify(state, "I", f"Edited value from {old_value} to {value}")


def delete_df(state, var_name, payload):
    index = payload["index"]
    state.local_data = state.local_data.drop(index=index)
    notify(state, "E", f"Deleted row at index '{index}'")

table_properties = {
    "class_name": "rows-bordered",
    "filter": True,
    "on_edit": edit_df,
    "on_delete": delete_df,
    "group_by[Days Till Due]": True,
}
pd.set_option('display.max_columns', None)

input_name_data_node_cfg = Config.configure_data_node(id="input_name")
message_data_node_cfg = Config.configure_data_node(id="message")

build_msg_task_cfg = Config.configure_task("build_msg", build_message, input_name_data_node_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])

input_name = "Taipy"
message = None
csv_node = None
path = None

x_range = range(1, 6)
data = {
    "Assignment": ("Please Enter a "),
    "Weight": ["CSV File"]
}

columns = "Assignment;Weight",

page = """
<|container container-styling|
<center>
Homework Queue 
</center>
|>

<center>
<|{data}|table|columns={columns[0]}|show_all|width=1000px|>
<|{columns}|toggle|>
</center>

<center>
<|Date|button|>
<|Points|button|>
<|Type|button|>
<|Weights|button|>
</center>

<center>
<|{path}|file_selector|label=Upload Homework|on_action=load_csv_file|extensions=.csv|hover_text=Load Homework|>
</center>
"""

Core().run()
scenario = tp.create_scenario(scenario_cfg)

stylekit = {
    "color_primary": "#03045E",
    "color_secondary": "#0077B6",
    "color_background_dark": "#48CAE4",
    "color_background_light": "#ADE8F4",
}
main_md = Markdown("""
# Daily Calorie Tracker""")
Gui(page).run(stylekit=stylekit)
