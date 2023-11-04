from SortedPriorityQueue import SortedPriorityQueue

my_queue = SortedPriorityQueue()

for index in my_queue._data:
    print(index)


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

data = pd.read_csv("Test Homework File - Sheet1.csv")
# print(data)
# for row in data.iterrows():
#     print(row[0], row[1])
# priority = 1 / (data['Assignment_Points'] / data['Total Points in Class(Including this assignment)'] *
#                 data['Assignment_Weight'] * (1 / data['Days Left Till Due']))
day_weight = 1
point_weight = 1
weight_weight = 0

priority = day_weight * data['Days Left Till Due'] + point_weight * data['Assignment_Points'] + weight_weight * data['Assignment_Weight']



data['Priority'] = priority
print(data)


for index in range(len(data)):
    my_queue.add(data.iloc[index, 5], data.iloc[index, 0])


prioritized_dict = {'Assignment_Name': [], 'Priority': []}
for index in range(len(my_queue)):
    key, value = my_queue.remove_min()
    prioritized_dict['Assignment_Name'].append(value)
    prioritized_dict['Priority'].append(key)
prioritized_data = pd.DataFrame(prioritized_dict)
print(prioritized_data)

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
