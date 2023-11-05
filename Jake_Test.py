import taipy as tp
from taipy import Core, Gui
from taipy.gui import notify
import pandas as pd

from prioritize import prioritize

def submit_homework(state):
    state.scenario.csv_node.write(state.csv_node)


def load_csv_file(state):
    local_data = pd.read_csv(state.path)

    # Create a new DataFrame with the first and last columns from the loaded data
    new_data = pd.DataFrame({
        "Assignment": local_data.iloc[:, 0],
        "Weight": local_data.iloc[:, -1]
    })
    print(new_data)
    # Replace the "Assignment" and "Weight" columns in state.data with the new data
    state.data[["Assignment", "Weight"]] = new_data
    #print(state.data)
    state.data = new_data


def delete_row(state, var_name, action, payload):
    old = payload["index"]
    state.data = state.data.drop(index=old)
    notify(state, "E", f"Deleted row at index '{old}'")


pd.set_option('display.max_columns', None)


input_name = "Taipy"
message = None
csv_node = None
path = None


data = pd.DataFrame({"Assignment": ["Please Enter a ",0,0,0,0,0,0,0,0,0,0,0,0], "Weight": ["CSV File",0,0,0,0,0,0,0,0,0,0,0,0]})

page = """
<|container container-styling|
<center>
Homework Queue 
</center>
|>

<center>
<|{data}|table|show_all|width=1000px|on_delete=delete_row|>
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

stylekit = {
    "color_primary": "#03045E",
    "color_secondary": "#0077B6",
    "color_background_dark": "#48CAE4",
    "color_background_light": "#ADE8F4",
}

Gui(page).run(stylekit=stylekit)
