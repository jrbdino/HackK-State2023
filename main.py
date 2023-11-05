
from taipy import Core, Gui
import pandas as pd
from prioritize import prioritize

pd.set_option('display.max_columns', None)
def load_csv_file(state):
    local_data = pd.read_csv(state.path)
    local_data = prioritize(local_data)
    new_data = pd.DataFrame({
        "Assignment": local_data.iloc[:, 0],
        "Weight": local_data.iloc[:, -1]
    })
    state.data[["Assignment", "Weight"]] = new_data
    state.data = new_data

path = None

data = pd.DataFrame({"Assignment": ["Please Enter a ",0,0,0,0,0,0,0,0,0,0,0,0], "Weight": ["CSV File",0,0,0,0,0,0,0,0,0,0,0,0]})

page = """
<|container container-styling|
<center>
Homework Queue 
</center>
|>

<center>
<|{data}|table|show_all|width=1000px|>
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
