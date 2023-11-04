import taipy as tp
from taipy import Config, Core, Gui
import pandas as pd
pd.set_option('display.max_columns', None)

def build_message(name):
    return f"Hello {name}!"

def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit()
    state.message = scenario.message.read()
def submit_homework(state):
    state.scenario.csv_node.write(state.csv_node)
def load_csv_file(state):
    data = pd.read_csv(state.path)
    print(data.columns)


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
    "Assignment": x_range,
    "Weight": [x*x for x in x_range]
}

columns = "Assignment;Weight", "Squared"

page = """
<|container container-styling|
<center>
Homework Queue 
</center>
|>

<|{data}|table|columns={columns[0]}|show_all|>
<|{columns}|toggle|>

<|Points|button|>
<|Date|button|>
<|Type|button|>
<|Weights|button|>

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

Gui(page).run(stylekit=stylekit)
